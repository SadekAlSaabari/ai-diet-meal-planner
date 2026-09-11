import os
import dotenv
import json
from typing import Any, Dict
from openai import OpenAI

dotenv.load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
        self.model = str(os.getenv("MODEL", "openai/gpt-oss-20b"))
        self.client = OpenAI(
                        api_key=self.api_key,
                        base_url=self.api_url
                    )

    def call_model_json(
            self, 
            prompt: str, 
            system_prompt: str = "You are a helpful assistant that responds strictly in JSON.") -> Dict[str, Any]:

        completion = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"}
        )

        raw_output = completion.choices[0].message.content or "{}"
        return json.loads(raw_output)