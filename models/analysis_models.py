from typing import Optional
from pydantic import BaseModel
from models.conversation_models import Question
from enum import Enum
from models.request_models import OrderDetails

#class PromptContext(BaseModel):
 #   subject: Optional[str] = None
  #  action: Optional[str] = None
   # location: Optional[str] = None
   # composition: Optional[str] = None
   # style: Optional[str] = None

#class PromptAnalysisResult(BaseModel):
#   prompt_context: PromptContext
#    complete: bool
#    questions: list[Question]

class AnalyzerOutput(BaseModel):
    questions: list[Question]
class AnalyzeResponse(BaseModel):
    order_details: OrderDetails
    user_prompt: str
    questions: list[Question]