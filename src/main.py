from src.utils.image_io import load_image
from src.agents.orchestrator import Orchestrator
from src.generation.response_builder import ResponseBuilder


def main():
    print("Agentic Fashion Color Assistant\n")

    image_path = "data/sample_images/test.jpg"
    user_text = "I want a smart casual outfit"

    image = load_image(image_path)

    orchestrator = Orchestrator()
    state = orchestrator.run(image, user_text)

    builder = ResponseBuilder()
    final_response = builder.build(state)

    print(final_response)

    print("\n--- Debug Info ---")
    print("Revision count:", state["revision_count"])


if __name__ == "__main__":
    main()
