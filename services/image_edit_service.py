from .openrouter_client import client
from dotenv import load_dotenv
import os
from openai import NotFoundError


load_dotenv()
print(client.base_url)
print(os.getenv("EDIT_MODEL"))
class ImageEditService:
    def edit(self, image,  prompt):
        try:
            response = client.images.generate(
        model=os.getenv("EDIT_MODEL"),
        prompt=prompt,
    )
        except NotFoundError as e:
            print(e.response.status_code)
            print(e.response.text)
            raise