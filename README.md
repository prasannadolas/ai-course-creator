
# Autonomous AI Course Creator

> **Using Google ADK & Gemini 2.0 Flash Lite**

## Project Overview
![Project Overview](diagram_folder/project_overview.png)

### Problem Statement

In today's rapidly evolving technological landscape, the demand for upskilling and high-quality educational content has never been higher. However, traditional instructional design remains a significant bottleneck. Creating a comprehensive course is a slow, manual, and resource-intensive process, often requiring teams of subject matter experts, writers, and editors weeks or months to plan, draft, review, and finalize content. This inability to scale content production efficiently leaves vast knowledge gaps unfilled in both corporate and academic settings.

### Solution Statement

The **Autonomous AI Course Creator** is designed to solve this content bottleneck by automating the end-to-end instructional design process. It is not merely a text generation tool, but a sophisticated **multi-agent system** that orchestrates a digital workforce of specialized AI agents. By mimicking a human team—with dedicated agents for curriculum planning, technical writing, assessment creation, and quality control critiquing—the system can take a single topic prompt and autonomously generate a high-quality, multi-module course package (including lessons, quizzes, and summaries) in minutes instead of weeks.

-----

## Core Concept & Value

### Why Agents? (Core Innovation)

Traditional LLM approaches often involve a single prompt like "Write a course on Python," which typically results in shallow, hallucinated, or unstructured content. This project leverages a Multi-Agent Architecture because instructional design is a multi-step workflow that requires different "modes of thinking."

  * **Separation of Concerns:** Just as a university has a separate Professor, Dean, and Exam Board, this system assigns distinct roles to different agents. This ensures that the entity creating the lesson is not the same one grading it, reducing bias and improving quality.
  * **Iterative Refinement:** The output of one agent (e.g., the Syllabus) becomes the input for the next (e.g., the Content Writer). This chaining allows for deeper context retention and more coherent long-form content generation.
  * **Scalability:** This architecture allows for "Modular Generation." Instead of hitting token limits by generating a whole book at once, the system can loop through modules, generating infinite content without losing quality.

### Key Features

  * **Sequential Multi-Agent Workflow:** Implements a linear pipeline where a Curriculum Architect, Content Professor, Reviewer (Dean), and Examiner work in a strict sequence to produce high-quality outputs.
  * **Turbo Modular Engine:** Features a sophisticated looping mechanism that generates content module-by-module. This avoids context window limits and ensures every single lesson is a "deep dive" rather than a summary.
  * **Native Google Search Grounding:** The Curriculum Agent is equipped with Google's native search tool, enabling it to fact-check syllabus topics against real-time 2025 trends and data.
  * **Dual Interface (Web & CLI):**
      * *Streamlit Web App:* A polished, user-friendly interface for end-users to generate and download professional PDF courses.
      * *Developer CLI:* A robust command-line tool for debugging, observing agent "thought processes," and generating structured file outputs.
  * **Professional PDF Export:** Uses CSS-styled HTML-to-PDF conversion to turn raw AI text into a beautifully formatted textbook-style document ready for distribution.
  * **Observability & Logging:** Built-in logging tracks every agent interaction, event ID, and state change, providing complete transparency into the AI's decision-making process.

-----

## Architecture

## Architectural Diagram
![Architecture Diagram](diagram_folder/Architecture.png) 

### Design Philosophy

The architecture of the Autonomous AI Course Creator is built on the principles of Modularity, Orchestration, and Reliability.

  * **Agentic Modularity:** Each agent is a self-contained unit with a specific "persona" and "toolset." The Curriculum Architect only cares about structure, while the Examiner only cares about validation. This prevents context bleeding, where an AI tries to do too much at once and degrades in quality.
  * **Centralized Orchestration:** Rather than agents talking chaotically to each other, a central Runner (powered by Google ADK) manages the state and flow. This ensures a deterministic output where Step A always leads to Step B, making the system reliable enough for production use.
  * **Stateless Execution with State Injection:** While the application uses `InMemorySessionService` for speed during a session, the architecture is designed to be stateless between runs. This allows the system to be deployed as a microservice or a cloud function without needing a persistent database for the core logic.

### High-Level Component Breakdown

**1. The Orchestrator (Runner)**
The "brain" of the operation. It initializes the session, injects the user's prompt, and calls the agents in the correct order. It manages the Turbo Modular Loop, iterating through the syllabus one module at a time.

**2. The Agent Workforce**

  * **Curriculum Agent:** Uses Google Search Grounding to research the topic and outputs a structured JSON-like list of modules.
  * **Content Agent (Professor):** Takes a specific module title and writes a deep-dive lesson with code examples.
  * **Review Agent (The Dean):** Acts as a quality gate. It takes the draft from the Professor and rewrites it for clarity, formatting, and tone.
  * **Quiz Agent (Examiner):** Reads the final lesson and generates a relevant quiz to test user understanding.

**3. The Memory Layer**

  * **Session Service:** Uses an in-memory store to hold the conversation history. This allows the Content Agent to "remember" what the Curriculum Agent planned, ensuring consistency across the entire course.

**4. The Presentation Layer**

  * **Streamlit UI:** Provides the frontend for user interaction and real-time feedback.
  * **PDF Engine:** A post-processing unit that compiles the markdown outputs from all agents into a single, styled PDF document.

 ![ER Diagram](diagram_folder/Er-diagram.png)

### Project Structure

```text
AI-COURSE-CREATOR/
├── course_agents/          # AI Agent Definitions
│   ├── content_agent.py    # Professor: Writes detailed lessons
│   ├── curriculum_agent.py # Architect: Plans the syllabus structure
│   ├── quiz_agent.py       # Examiner: Generates assessments
│   └── review_agent.py     # Dean: Critiques and polishes content
│
├── course_outputs/         # Output Directory (Generated at runtime)
│   └── [Topic_Name]/
│       ├── Syllabus_Overview.md
│       ├── Module_1/
│       │   ├── lesson.md
│       │   └── quiz.md
│
├── tools/                  # Helper Tools
│   ├── file_writer_tool.py # Handles file saving operations
│   └── search_tool.py      # (Optional) External search utility
│
├── utils/                  # Configuration & Utilities
│   ├── gemini_client.py    # Gemini model wrapper
│   └── logger.py           # System logging setup
│
├── venv/                   # Virtual Environment
├── .env                    # API Keys (Excluded from git)
├── .gitignore              # Git ignore rules
├── check_models.py         # Diagnostic script for API access
├── cli_runner.py           # CLI entry point (Developer Mode)
├── config.py               # Central config (Model selection)
├── requirements.txt        # Python dependencies
└── streamlit_app.py        # Web App entry point (User Mode)
```

-----

## Workflow
![Workflow Diagram](diagram_folder/Workflow.png)

The system follows a structured, automated multi-agent workflow:

1.  **Initialization:** A user submits a topic prompt and target audience via the Streamlit Web UI or the CLI.
2.  **Planning Phase:** The Curriculum Architect (Agent 1) uses Google Search Grounding to research the topic and autonomously generates a structured, 5-module syllabus outline.
3.  **Modular Execution Loop:** The orchestrator enters a "Turbo Loop," processing each module one by one:
      * *Drafting:* The Content Professor (Agent 2) writes a detailed first draft of the lesson, including code examples and deep explanations.
      * *Critique & Polish:* The Reviewer/Dean (Agent 3) takes the draft, fixes grammar, improves formatting, and produces a "Final Polish" version.
      * *Assessment:* The Examiner (Agent 4) reads the final lesson and generates a specific 3-question quiz for that module.
4.  **Compilation:** All generated assets (Syllabus, Lessons, Quizzes) are aggregated into a single master document.
5.  **Finalization:** The system converts the master markdown document into a CSS-styled professional PDF and presents it to the user for download.

-----

## Essential Tools and Utilities

The system is built upon a robust, modern backend stack designed for reliable agent orchestration and high-speed AI inference.

**Core AI & Orchestration**

  * **Google Gemini API (Model: gemini-2.0-flash-lite):** The central "brain" chosen for its balance of high-speed inference and strong reasoning capabilities, essential for powering parallel agents and critique loops.
  * **Google Agent Development Kit (ADK):** The foundational framework for building, managing, and orchestrating the multi-agent system.
  * **Python 3.13:** The primary language serving as the central nervous system and logic handler.

**Application & Interface**

  * **Streamlit:** The framework used to build the interactive web application, providing a clean and responsive user interface for course generation.
  * **XHTML2PDF & Markdown2:** Utilities for converting raw AI-generated markdown text into professionally styled PDF documents.

**Data & Memory**

  * **InMemorySessionService:** A lightweight session management service provided by ADK to maintain conversation history and context during the generation pipeline.

**DevOps & Security**

  * **python-dotenv:** Ensures secure management of API keys and environment variables.
  * **Logging (Standard Library):** Integrated for observability, tracing agent execution paths and debugging multi-agent interactions in the CLI.

-----

## Installation

### Prerequisites

  * Python 3.10+
  * Google AI Studio API Key
  * Git

### Step-by-Step Setup

**1. Clone the Repository**

```bash
git clone https://github.com/prasannadolas/ai-course-creator
cd ai-course-creator
```

**2. Set Up Virtual Environment**
*Windows:*

```bash
python -m venv venv
.\venv\Scripts\activate
```

*macOS/Linux:*

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure Environment**
Create a `.env` file in the root directory and add your Google API key:

```text
GOOGLE_API_KEY=your_actual_google_api_key
```

### Running the Application

**Option 1: Web Interface (Streamlit)**
For the full graphical user experience with PDF downloads:

```bash
streamlit run streamlit_app.py
```

*Access the UI at `http://localhost:8501`*

**Option 2: Command Line Interface (CLI)**
For developer debugging and structured file generation:

```bash
python cli_runner.py
```

*Follow the terminal prompts to generate your course.*

-----

## Conclusion & Value

The **Autonomous AI Course Creator** proves that complex, knowledge-intensive tasks like instructional design can be effectively automated through a sophisticated multi-agent system architecture. By grounding the AI with real-time search data (Goggle Grounding) and implementing adversarial feedback loops (via the Reviewer Agent), we have built a system that balances the speed of AI with the quality control of human oversight.

For Learning & Development (L\&D) teams, educators, and EdTech platforms, this tool transforms content creation from a slow, expensive bottleneck into a scalable utility. It offers a significant acceleration in speed-to-market and democratizes access to rapid, high-quality curriculum development, ensuring that educational material can keep pace with the speed of technological innovation.

----