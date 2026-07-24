import os
import requests
from io import BytesIO
from dotenv import load_dotenv
from openai import OpenAI
from .openrouter_client import client
load_dotenv()
print(os.getenv("OPENROUTER_API_KEY")[:15])
print(os.getenv("MODEL_NAME"))

def generate_image(prompt: str, reference_image=None):
    if reference_image:
        image = download_image(reference_image)
        response= client.images.edit(
            model=os.getenv("EDIT_MODEL"),
            image=image_file,
            prompt=prompt
        )
    else:
        response = client.images.generate(
            model=os.getenv("MODEL_NAME"),
            prompt=prompt
        )

    return response
def download_image(url):
    response = requests.get(url)
    return BytesIO(response.content)