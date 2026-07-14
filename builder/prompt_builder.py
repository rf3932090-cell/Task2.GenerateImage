from builder.templates import PROMPT_TEMPLATE
from models.request_models import GenerateRequest
class PromptBuilder:
   def build_prompt(self, request: GenerateRequest):

    context = request.prompt_context

    prompt = PROMPT_TEMPLATE.format(
        product_type=request.order_details.product_type,
        medium_style=request.order_details.medium_style,
        color_palette=request.order_details.color_palette,
        dimensions=f"{request.order_details.dimensions.width_cm}x{request.order_details.dimensions.height_cm}",
        aspect_ratio=request.order_details.dimensions.aspect_ratio,

        user_prompt=request.user_prompt,

        subject=context.subject or "",
        action=context.action or "",
        location=context.location or "",
        composition=context.composition or "",
        style=context.style or "",
    )

    return prompt