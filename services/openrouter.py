import os

from dotenv import load_dotenv
from openai import OpenAI
from .openrouter_client import client
load_dotenv()
print(os.getenv("OPENROUTER_API_KEY")[:15])
print(os.getenv("MODEL_NAME"))

def generate_image(prompt: str):

    response = client.images.generate(
        model=os.getenv("MODEL_NAME"),
        prompt=prompt
    )

    return response
