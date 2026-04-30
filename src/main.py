# src/main.py

from src.utils.image_io import load_image
from src.utils.color_analysis import extract_dominant_colors, get_palette_hex
from src.utils.color_naming import simple_color_name
from src.knowledge.rule_loader import load_rules
from src.knowledge.rule_matcher import find_best_match


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"
    image = load_image(image_path)

    colors = extract_dominant_colors(image, k=3)
    palette = get_palette_hex(colors)

    print("Detected colors:", palette)

    # convert first color to name
    base_color = simple_color_name(palette[0])

    rules = load_rules()
    result = find_best_match([base_color], rules)

    print("\nBase color:", result["base_color"])
    print("Recommended matches:", result["matches"])
    print("Style note:", result["style"])


if __name__ == "__main__":
    main()
