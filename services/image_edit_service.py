from .avalai_client import client
from dotenv import load_dotenv
import os
from openai import NotFoundError
import openai

class ImageEditService:
    def edit(self, image,  prompt):
        response = client.images.edit(
        model="openai/gpt-image-2",
        image=image,
    prompt=prompt,
)
        return response