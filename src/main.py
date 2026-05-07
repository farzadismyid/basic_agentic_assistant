# src/main.py

from src.utils.image_io import load_image
from src.agents.orchestrator import Orchestrator


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"
    user_text = "I want a smart casual outfit"

    image = load_image(image_path)

    orchestrator = Orchestrator()
    result = orchestrator.run(image, user_text)

    print("\n--- Final Agentic State ---")
    print("Visual:", result["visual_output"])
    print("Knowledge:", result["knowledge_output"])
    print("Critic:", result["critic_output"])
    print("Revision count:", result["revision_count"])


if __name__ == "__main__":
    main()
