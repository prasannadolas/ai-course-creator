import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: API Key not found.")
else:
    print(f"✅ API Key found: {api_key[:5]}********")
    
    # Configure the library
    genai.configure(api_key=api_key)

    print("\n🔍 Fetching available models for this key...")
    try:
        count = 0
        for m in genai.list_models():
            # We only care about models that can generate text (content)
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
                count += 1
        
        if count == 0:
            print("⚠️ No content generation models found. Check your API key billing/region.")
            
    except Exception as e:
        print(f"❌ Error listing models: {e}")