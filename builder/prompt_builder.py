from builder.templates import PROMPT_TEMPLATE
from builder.concepts import PRODUCT_CONCEPTS
from builder.enhancer import DictionaryEnhancer
from builder.models import GenerateRequest

class PromptBuilder:
    def __init__(self):
        self.enhancer = DictionaryEnhancer()
    
    def build_prompt(self, request: GenerateRequest) -> str:
        prompt = PROMPT_TEMPLATE.format(
            product_type = request.order_details.product_type,
            medium_style = request.order_details.medium_style,
            color_palette = request.order_details.color_palette,
            dimensions = f"{request.order_details.dimensions.width_cm}x{request.order_details.dimensions.height_cm}",
            aspect_ratio = request.order_details.dimensions.aspect_ratio,
            user_prompt = request.user_prompt,
        )
        return prompt
    