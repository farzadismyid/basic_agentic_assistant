from PIL import Image


def load_image(path: str) -> Image.Image:
    image = Image.open(path).convert("RGB")
    return image


    colors = kmeans.cluster_centers_.astype(int)
    return colors


def rgb_to_hex(color):
    return '#%02x%02x%02x' % tuple(color)


def get_palette_hex(colors):
    return [rgb_to_hex(c) for c in colors]
