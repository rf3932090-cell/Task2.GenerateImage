import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print(os.getenv("OPENROUTER_API_KEY")[:15])
print(os.getenv("MODEL_NAME"))
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
def generate_image(prompt: str):

    response = client.images.generate(
        model=os.getenv("MODEL_NAME"),
        prompt=prompt
    )

    return response
