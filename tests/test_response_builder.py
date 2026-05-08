# tests/test_response_builder.py

from src.generation.response_builder import ResponseBuilder


def test_response_builder():
    builder = ResponseBuilder()

    state = {
        "knowledge_output": {
            "base_color": "blue",
            "matches": ["white", "grey"],
            "style": "Blue works well with neutral colors.",
            "used_external": True
        },
        "critic_output": {
            "grounding_score": 1.0
        }
    }

    response = builder.build(state)

    assert isinstance(response, str)
    assert "blue" in response
