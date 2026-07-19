from fastapi import FastAPI, HTTPException
from fastapi import UploadFile, File, Form
from builder.prompt_builder import PromptBuilder
from services.openrouter import generate_image
from models.request_models import GenerateRequest, GenerateImageRequest
from models.analysis_models import AnalyzeResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import Response
import base64
from analysis.analyzer import PromptAnalyzer
from services.image_edit_service import ImageEditService

app = FastAPI(
    title="Image Generation API",
    version = "1.0.0"
)

prompt_builder = PromptBuilder()    

analyzer = PromptAnalyzer()


@app.get("/")
def root():
    return {
        "message": "Image Generation API is running."
    }
@app.post("/analyze")
def analyze(request: GenerateRequest):
    try:
        result = analyzer.analyze(request)
        return AnalyzeResponse(
            order_details = request.order_details,
            user_prompt = request.user_prompt,
            questions = result.questions
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
@app.post("/generate")
def generate(request: GenerateImageRequest):
    try:
        
        prompt = prompt_builder.build_prompt(request)
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
       

@app.post("/edit")
def edit(image: UploadFile, prompt: str):
    image_edit_service = ImageEditService()
    image = image_edit_service.edit((
            image.filename,
            image.file,
            image.content_type,
        ), prompt)
    return image
