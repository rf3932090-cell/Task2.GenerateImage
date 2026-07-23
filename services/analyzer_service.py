from dotenv import load_dotenv
import os
import json

from .openrouter_client import client
from analysis.analysis_prompt import ANALYSIS_PROMPT

load_dotenv()


class PromptAnalysisService:

    def __init__(self):
        self.client = client

    def analyze(self, request: dict):
        request_json = json.dumps(request, indent=2)

        response = self.client.chat.completions.create(
            model="google/gemini-2.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": ANALYSIS_PROMPT,
                },
                {
                    "role": "user",
                    "content": request_json,
                },
            ],
            temperature=0,
        )

        return json.loads(response.choices[0].message.content)