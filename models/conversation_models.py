from typing import Optional
from pydantic import BaseModel
from enum import Enum

class PromptField(str, Enum):
    subject = "subject"
    action = "action"
    location = "location"
    composition = "composition"
    style = "style"
class Question(BaseModel):
    field: PromptField
    question: str