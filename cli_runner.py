import asyncio
import time
import os
import re
from datetime import datetime
from types import SimpleNamespace

# Import ADK components
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Import your Agents
from course_agents.curriculum_agent import curriculum_agent
from course_agents.content_agent import content_agent
from course_agents.review_agent import review_agent
from course_agents.quiz_agent import quiz_agent

# --- HELPER FUNCTIONS ---
def wrap_message(text: str):
    return SimpleNamespace(role="user", parts=[SimpleNamespace(text=text)])

def extract_text(event):
    try:
        if event.content and event.content.parts:
            return event.content.parts[0].text
    except AttributeError:
        pass
    return None

def create_main_folder(topic):
    """Creates the main course folder based on the topic name."""
    safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '_', '-')).rstrip()
    safe_topic = safe_topic.replace(" ", "_")
    
    base_path = "course_outputs"
    # Example: course_outputs/Python_Course
    full_path = os.path.join(base_path, safe_topic)
    
    os.makedirs(full_path, exist_ok=True)
    return full_path

def create_module_folder(base_folder, module_name):
    """Creates a sub-folder for a specific module."""
    safe_name = "".join(c for c in module_name if c.isalnum() or c in (' ', '_', '-')).rstrip()
    safe_name = safe_name.replace(" ", "_")[:50] # Limit length
    
    module_path = os.path.join(base_folder, safe_name)
    os.makedirs(module_path, exist_ok=True)
    return module_path

def save_file(folder, filename, content):
    """Saves a file to the specific folder."""
    file_path = os.path.join(folder, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    # Print a nice tree structure log
    print(f"      ├── 📄 {filename}")

def parse_modules_from_syllabus(syllabus_text):
    """
    Simple parser to extract module titles from the syllabus text.
    It looks for lines starting with "Module 1:", "1.", "- Module", etc.
    """
    modules = []
    lines = syllabus_text.split('\n')
    for line in lines:
        clean_line = line.strip()
        # Regex to find lines that look like module headers
        # Matches: "Module 1: Title", "1. Title", "**Module 1**"
        if re.match(r'^(?:Module\s+\d+|Unit\s+\d+|\d+\.)[:\s-]', clean_line, re.IGNORECASE):
            # Clean up formatting (** bold markers etc)
            clean_title = clean_line.replace('*', '').strip()
            modules.append(clean_title)
    
    # Fallback if AI didn't format it as a list
    if not modules:
        return ["Module_1_Fundamentals", "Module_2_Core_Concepts", "Module_3_Advanced_Topics", "Module_4_Practical_Applications", "Module_5_Future_Trends"]
    
    return modules[:5] # Limit to 5 modules to save time/cost

# --- MAIN PIPELINE ---
async def run_cli_pipeline():
    print("\n🎓 === AI COURSE CREATOR (MODULAR EDITION) === 🎓")
    
    # 1. Setup
    topic = input("Enter Course Topic: ")
    audience = input("Enter Target Audience: ")
    if not topic: return

    output_folder = create_main_folder(topic)
    print(f"\n📂 Course Root: {output_folder}")

    session = InMemorySessionService()
    session_id = "cli_session"
    user_id = "cli_user"
    await session.create_session(session_id=session_id, user_id=user_id, app_name="cli_course_creator")

    # --- PHASE 1: SYLLABUS ---
    print("\n1️⃣  Designing Syllabus...")
    syllabus_text = ""
    runner = Runner(agent=curriculum_agent, session_service=session, app_name="cli_course_creator")
    msg = wrap_message(f"Create a syllabus for '{topic}' for {audience}. List exactly 5 modules. Format as 'Module X: Title'.")
    
    async for event in runner.run_async(session_id=session_id, user_id=user_id, new_message=msg):
        if event.is_final_response():
            syllabus_text = extract_text(event)
    
    save_file(output_folder, "Syllabus_Overview.md", syllabus_text)
    
    # Extract modules to iterate over
    modules = parse_modules_from_syllabus(syllabus_text)
    print(f"   └── Found {len(modules)} modules to generate.")
    time.sleep(10) # Increased initial pause

    # --- PHASE 2: MODULE GENERATION LOOP ---
    for i, module_title in enumerate(modules):
        print(f"\n   👉 Generating: {module_title}...")
        
        # Create folder: course_outputs/.../Module_1_Name
        mod_folder = create_module_folder(output_folder, module_title)

        # A. DETAILED LESSON (The Deep Dive)
        runner = Runner(agent=content_agent, session_service=session, app_name="cli_course_creator")
        draft_text = ""
        prompt = f"""
        Write the FULL DETAILED LESSON for '{module_title}'.
        - This must be a deep dive.
        - Include 'Practical Code Examples' (if technical).
        - CRITICAL: Every code block MUST be immediately followed by a detailed explanation of what the code does.
        - Include a 'Common Pitfalls' section.
        - Write at least 500 words.
        """
        async for event in runner.run_async(session_id=session_id, user_id=user_id, new_message=wrap_message(prompt)):
            if event.is_final_response(): draft_text = extract_text(event)
        
        # 🟢 SAFETY PAUSE 1
        time.sleep(10)

        # Send Draft to Reviewer
        final_lesson = ""
        runner_rev = Runner(agent=review_agent, session_service=session, app_name="cli_course_creator")
        rev_prompt = "Review this lesson. Improve structure, add bolding to key terms, and ensure code blocks are formatted."
        
        async for event in runner_rev.run_async(session_id=session_id, user_id=user_id, new_message=wrap_message(rev_prompt)):
            if event.is_final_response(): final_lesson = extract_text(event)
        
        if final_lesson:
            save_file(mod_folder, "lesson.md", final_lesson)
        
        # 🟢 SAFETY PAUSE 2
        time.sleep(10)

        # B. QUIZ (Specific to this module)
        quiz_text = ""
        runner_quiz = Runner(agent=quiz_agent, session_service=session, app_name="cli_course_creator")
        prompt = f"Create a short 5-question quiz specifically for '{module_title}' based on the lesson above."
        
        async for event in runner_quiz.run_async(session_id=session_id, user_id=user_id, new_message=wrap_message(prompt)):
            if event.is_final_response(): quiz_text = extract_text(event)
            
        if quiz_text:
            save_file(mod_folder, "quiz.md", quiz_text)
        
        # 🟢 SAFETY PAUSE 3 (Longer cooldown before next module)
        print("      ⏳ Cooling down API (30s)...")
        time.sleep(30) 

    print(f"\n✅ SUCCESS! Course generated in: {output_folder}")

if __name__ == "__main__":
    asyncio.run(run_cli_pipeline())