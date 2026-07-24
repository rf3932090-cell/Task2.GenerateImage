from builder.templates import PROMPT_TEMPLATE
from models.request_models import GenerateImageRequest
from .concepts import PRODUCT_CONCEPTS
class PromptBuilder:

    def _build_clarifications(self, answers):
        if not answers:
            return "None"

        return "\n\n".join(
            f"{answer.field}:\n{answer.answer}"
            for answer in answers
        )
    def build_prompt(self, request: GenerateImageRequest):

        product_type = request.order_details.product_type
        product_concept = PRODUCT_CONCEPTS.get(
            product_type, {}
        ).get(
            "prompt_context",
            ""
        )


        prompt = PROMPT_TEMPLATE.format(
            product_type=product_type,
            product_concept=product_concept,
            medium_style=request.order_details.medium_style,
            color_palette=request.order_details.color_palette,
            dimensions=f"{request.order_details.dimensions.width_cm}x{request.order_details.dimensions.height_cm}",
            aspect_ratio=request.order_details.dimensions.aspect_ratio,

            user_prompt=request.user_prompt,
            clarifications = self._build_clarifications(request.answers)        )

        return prompt