# src/utils/captioning.py

from PIL import Image
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText


MODEL_ID = "microsoft/Florence-2-base"


processor = AutoProcessor.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)

model = AutoModelForImageTextToText.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)


def generate_caption(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")

    prompt = "<CAPTION>"

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=50
        )

    generated_text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return generated_text
