from typing import Optional
from pydantic import BaseModel
from models.conversation_models import Question

class PromptContext(BaseModel):
    subject: Optional[str] = None
    action: Optional[str] = None
    location: Optional[str] = None
    composition: Optional[str] = None
    style: Optional[str] = None

class PromptAnalysisResult(BaseModel):
    prompt_context: PromptContext
    complete: bool
    questions: list[Question]
