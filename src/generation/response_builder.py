# src/generation/response_builder.py

class ResponseBuilder:
    def __init__(self):
        pass

    def build(self, state):
        knowledge = state["knowledge_output"]
        critic = state["critic_output"]

        base_color = knowledge["base_color"]
        matches = knowledge["matches"]
        style = knowledge["style"]

        response = []

        response.append(
            f"The detected main color is {base_color}."
        )

        response.append(
            f"Recommended matching colors: {', '.join(matches)}."
        )

        response.append(
            f"Style advice: {style}"
        )

        if knowledge["used_external"]:
            response.append(
                "Recommendations were grounded using external fashion rules."
            )
        else:
            response.append(
                "Recommendations were generated using internal matching logic."
            )

        response.append(
            f"Grounding score: {critic['grounding_score']:.2f}"
        )

        return "\n".join(response)
