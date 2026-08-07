from PIL import Image


def load_image(path: str) -> Image.Image:
    image = Image.open(path).convert("RGB")
    return image
