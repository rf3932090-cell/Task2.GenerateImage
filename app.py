from fastapi import FastAPI, HTTPException
from builder.prompt_builder import PromptBuilder
from services.openrouter import generate_image
from builder.models import GenerateRequest
from fastapi.responses import HTMLResponse
from fastapi.responses import Response
import base64
app = FastAPI(
    title="Image Generation API",
    version = "1.0.0"
)

prompt_builder = PromptBuilder()    



@app.get("/")
def root():
    return {
        "message": "Image Generation API is running."
    }

@app.post("/generate", response_class=HTMLResponse)
def generate(request: GenerateRequest):
    try:
        #Build Prompt
        prompt = prompt_builder.build_prompt(request)

        #Generate Image
        response = generate_image(prompt)
        image = response.data[0].b64_json

        image_bytes = base64.b64decode(image)

        return Response(
            content=image_bytes,
            media_type="image/png"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

