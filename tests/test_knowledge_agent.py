
from src.agents.knowledge_agent import KnowledgeAgent


def test_knowledge_agent():
    agent = KnowledgeAgent()

    visual_output = {
        "palette": ["#1f3a5f"],
        "color_confidence": 0.8
    }

    result = agent.analyze(visual_output, "smart casual outfit")

    assert "matches" in result
    assert isinstance(result["used_external"], bool)
