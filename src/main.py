# src/main.py

from src.utils.image_io import load_image
from src.agents.visual_agent import VisualAgent
from src.agents.knowledge_agent import KnowledgeAgent


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"
    user_text = "I want a smart casual outfit"

    image = load_image(image_path)

    visual_agent = VisualAgent()
    visual_output = visual_agent.analyze(image)

    knowledge_agent = KnowledgeAgent()
    knowledge_output = knowledge_agent.analyze(visual_output, user_text)

    print("\n--- Visual Agent ---")
    print(visual_output)

    print("\n--- Knowledge Agent ---")
    print(knowledge_output)


if __name__ == "__main__":
    main()
