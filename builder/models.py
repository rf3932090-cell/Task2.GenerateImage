from pydantic import BaseModel
from typing import Optional

class Dimensions(BaseModel):
    width_cm: int
    height_cm: int
    aspect_ratio: str

class ReferenceImage(BaseModel):
    file_url: Optional[str] = None
    mime_type: Optional[str] = None

class OrderDetails(BaseModel):
    product_type: str
    medium_style: str
    color_palette: str
    dimensions: Dimensions
    reference_image: Optional[ReferenceImage] = None

class GenerateRequest(BaseModel):
    order_details: OrderDetails
    user_prompt: str

    