# src/main.py

from src.utils.image_io import load_image
from src.utils.color_analysis import extract_dominant_colors, get_palette_hex


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"  # add your own image here
    image = load_image(image_path)

    colors = extract_dominant_colors(image, k=3)
    palette = get_palette_hex(colors)

    print("Detected colors:", palette)


if __name__ == "__main__":
    main()
