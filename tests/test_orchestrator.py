
from src.utils.image_io import load_image
from src.agents.orchestrator import Orchestrator


def test_orchestrator_runs():
    image = load_image("data/sample_images/test.jpg")

    orchestrator = Orchestrator()
    result = orchestrator.run(image, "smart casual outfit")

    assert "visual_output" in result
    assert "knowledge_output" in result
    assert "critic_output" in result
    assert "revision_count" in result
