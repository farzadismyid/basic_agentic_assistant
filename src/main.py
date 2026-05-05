# src/main.py

from src.utils.image_io import load_image
from src.agents.visual_agent import VisualAgent
from src.agents.knowledge_agent import KnowledgeAgent
from src.agents.critic_agent import CriticAgent


def main():
    print("Agentic Fashion Color Assistant")

    image_path = "data/sample_images/test.jpg"
    user_text = "I want a smart casual outfit"

    image = load_image(image_path)

    visual_agent = VisualAgent()
    knowledge_agent = KnowledgeAgent()
    critic_agent = CriticAgent()

    # Step 1: Visual
    visual_output = visual_agent.analyze(image)

    # Step 2: Knowledge
    knowledge_output = knowledge_agent.analyze(visual_output, user_text)

    # Step 3: Critic
    critic_output = critic_agent.evaluate(knowledge_output, user_text)

    # --- Agentic Loop (1 iteration) ---
    if critic_output["needs_revision"]:
        print("\n[Critic] Revision triggered...")

        # force external knowledge if first attempt was weak
        visual_output["color_confidence"] = 0.3

        knowledge_output = knowledge_agent.analyze(visual_output, user_text)
        critic_output = critic_agent.evaluate(knowledge_output, user_text)

    print("\n--- Final Output ---")
    print("Knowledge:", knowledge_output)
    print("Critic:", critic_output)


if __name__ == "__main__":
    main()
