# src/agents/critic_agent.py

class CriticAgent:
    def __init__(self):
        pass

    def evaluate(self, knowledge_output, user_text=None):
        matches = knowledge_output["matches"]
        used_external = knowledge_output["used_external"]
        retrieval_confidence = knowledge_output["retrieval_confidence"]

        # --- Decision variables ---
        completeness = self._check_completeness(matches)
        grounding = self._check_grounding(used_external, retrieval_confidence)
        needs_revision = self._decide_revision(completeness, grounding)

        return {
            "completeness_score": completeness,
            "grounding_score": grounding,
            "needs_revision": needs_revision
        }

    def _check_completeness(self, matches):
        return min(len(matches) / 4, 1.0)

    def _check_grounding(self, used_external, retrieval_confidence):
        if used_external:
            return retrieval_confidence
        return 0.5

    def _decide_revision(self, completeness, grounding):
        if completeness < 0.5:
            return True
        if grounding < 0.5:
            return True
        return False
