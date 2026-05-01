from src.utils.image_io import load_image
from src.agents.visual_agent import VisualAgent


def test_visual_agent():
    image = load_image("data/sample_images/test.jpg")
    agent = VisualAgent()

    result = agent.analyze(image)

    assert "palette" in result
    assert isinstance(result["needs_caption"], bool)
