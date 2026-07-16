from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from enum import Enum
from models.conversation_models import Answer

class ProductType(str, Enum):
    Wall_Art = "Wall_Art"
    Mug = "Mug"
    Carpet = "Carpet"
    Canvas = "Canvas"

class Dimensions(BaseModel):
    width_cm: int = Field(gt=0)
    height_cm: int = Field(gt=0)
    aspect_ratio: str = Field(min_length=3)

class ReferenceImage(BaseModel):
    file_url: Optional[HttpUrl]= None
    mime_type: Optional[str] = None

class OrderDetails(BaseModel):
    product_type: ProductType
    medium_style: str = Field(min_length=1)
    color_palette: str = Field(min_length=1)
    dimensions: Dimensions
    reference_image: Optional[ReferenceImage] = None

class GenerateRequest(BaseModel):
    order_details: OrderDetails
    user_prompt: str = Field(
        min_length=5,
        max_length=500
    )
    #prompt_context: Optional[PromptContext] = None

    
class GenerateImageRequest(BaseModel):
    order_details: OrderDetails
    user_prompt: str
    answers: list[Answer]