from src.agents.critic_agent import CriticAgent


def test_critic_agent():
    agent = CriticAgent()

    knowledge_output = {
        "matches": ["white", "black"],
        "used_external": False,
        "retrieval_confidence": 0.5
    }

    result = agent.evaluate(knowledge_output)

    assert "needs_revision" in result
    assert isinstance(result["needs_revision"], bool)
    