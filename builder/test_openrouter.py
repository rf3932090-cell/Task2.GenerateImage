from services.openrouter import generate_image
import base64

prompt = """
A photorealistic ceramic coffee mug on a wooden table,
minimalist style,
soft studio lighting,
high quality.
"""

response = generate_image(prompt)
import base64


img_data = response.data[0].model_dump()

image_base64 = img_data["b64_json"]

image_bytes = base64.b64decode(image_base64)

with open("coffee_mug.jpg", "wb") as f:
    f.write(image_bytes)

print("saved: coffee_mug.jpg")