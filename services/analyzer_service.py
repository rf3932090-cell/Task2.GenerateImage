from google import genai
from dotenv import load_dotenv
import os
import json

from analysis.analysis_prompt import ANALYSIS_PROMPT

load_dotenv()


class PromptAnalysisService:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = os.getenv("ANALYZER_MODEL")

        print("MODEL =", self.model)


    def analyze(self, request: dict):
        request_json = json.dumps(request, indent=2)

        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                ANALYSIS_PROMPT,
                request_json
            ]
        )

        return json.loads(response.text)