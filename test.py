import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Force load the .env file
load_dotenv(override=True)

api_key = os.getenv("GROQ_API_KEY")
base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
model = os.getenv("MODEL", "openai/gpt-oss-20b")

print(f"--> Base URL being used: {base_url!r}")
print(f"--> Model ID being requested: {model!r}")
print(f"--> Key prefix: {api_key[:8] if api_key else 'NONE'}...")

client = OpenAI(api_key=api_key, base_url=base_url)

try:
    models = client.models.list()
    available_ids = [m.id for m in models.data]
    print("\n[SUCCESS] Connected to Groq! Available models on your account:")
    for m_id in sorted(available_ids):
        print(f"  - {m_id}")
        
    if model in available_ids:
        print(f"\nModel '{model}' is present and active.")
    else:
        print(f"\n[WARNING] Model '{model}' is NOT in the list returned by Groq!")
except Exception as e:
    print(f"\n[ERROR] Request failed: {e}")