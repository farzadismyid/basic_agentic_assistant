
from src.utils.image_io import load_image
from src.agents.visual_agent import VisualAgent


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"
    image = load_image(image_path)

    visual_agent = VisualAgent()
    result = visual_agent.analyze(image)

    print("\n--- Visual Agent Output ---")
    print("Palette:", result["palette"])
    print("Color confidence:", round(result["color_confidence"], 2))
    print("Image quality:", round(result["image_quality"], 2))
    print("Needs captioning:", result["needs_caption"])


if __name__ == "__main__":
    main()
