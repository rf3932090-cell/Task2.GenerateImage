from builder.templates import PROMPT_TEMPLATE
from models.request_models import GenerateImageRequest
class PromptBuilder:
    def build_prompt(self, request: GenerateImageRequest):

        answer_map = {
            answer.field.value: answer.answer
            for answer in request.answers
        }

        prompt = PROMPT_TEMPLATE.format(
            product_type=request.order_details.product_type,
            medium_style=request.order_details.medium_style,
            color_palette=request.order_details.color_palette,
            dimensions=f"{request.order_details.dimensions.width_cm}x{request.order_details.dimensions.height_cm}",
            aspect_ratio=request.order_details.dimensions.aspect_ratio,

            user_prompt=request.user_prompt,

            subject=answer_map.get("subject", ""),
            action=answer_map.get("action", ""),
            location=answer_map.get("location", ""),
            composition=answer_map.get("composition", ""),
            style=answer_map.get("style", ""),
        )

        return prompt