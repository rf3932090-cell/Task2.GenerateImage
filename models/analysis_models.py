from typing import Optional
from pydantic import BaseModel
from models.conversation_models import Question
from enum import Enum
from models.request_models import OrderDetails
from typing import Literal


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

#class AnalyzerOutput(BaseModel):
#    questions: list[Question]
#class AnalyzeResponse(BaseModel):
#   order_details: OrderDetails
#   user_prompt: str
#   questions: list[Question]

class checkListStatus(str, Enum):
    complete = "complete"
    missing = "missing"
class ChecklistItem(BaseModel):
    name: str
    status: Literal["complete", "missing"]


class Question(BaseModel):
    field: str
    question: str


class AnalyzerOutput(BaseModel):
    checklist: list[ChecklistItem]
    questions: list[Question]