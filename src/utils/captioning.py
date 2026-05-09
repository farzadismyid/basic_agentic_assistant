# src/utils/captioning.py

from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import torch


MODEL_ID = "microsoft/Florence-2-base"

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)


def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")

    prompt = "<CAPTION>"

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    )

    generated_ids = model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=50
    )

    generated_text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return generated_text
