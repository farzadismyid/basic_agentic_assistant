# src/utils/captioning.py

from PIL import Image
import torch

from transformers import (
    AutoProcessor,
    AutoModelForCausalLM
)

MODEL_ID = "microsoft/Florence-2-base"

processor = AutoProcessor.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)

# ---- FIX ----
if not hasattr(model.config, "forced_bos_token_id"):
    model.config.forced_bos_token_id = None


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
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=50,
            do_sample=False
        )

    generated_text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return generated_text
