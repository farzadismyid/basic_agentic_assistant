# src/main.py

from src.utils.image_io import load_image
from src.agents.orchestrator import Orchestrator
from src.generation.response_builder import ResponseBuilder


def main():
    print("Agentic Fashion Color Assistant\n")

    image_path = "data/sample_images/test.jpg"
    user_text = "I want a smart casual outfit"

    image = load_image(image_path)

    orchestrator = Orchestrator()

    state = orchestrator.run(
        image,
        image_path=image_path,
        user_text=user_text
    )

    builder = ResponseBuilder()
    final_response = builder.build(state)

    print(final_response)

    caption = state["visual_output"]["caption"]

    if caption:
        print("\nGenerated caption:")
        print(caption)

    print("\n--- Debug Info ---")
    print("Revision count:", state["revision_count"])


if __name__ == "__main__":
    main()
