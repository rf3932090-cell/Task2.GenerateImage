from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print(client.models.list())
response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)