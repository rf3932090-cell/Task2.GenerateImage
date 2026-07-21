from dotenv import load_dotenv
from openai import OpenAI
import os
import httpx

load_dotenv()
client = OpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key=os.getenv("AVALAI_API_KEY"),
)
