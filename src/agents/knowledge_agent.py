
from src.knowledge.rule_loader import load_rules
from src.knowledge.rule_matcher import find_best_match
from src.utils.color_naming import simple_color_name


class KnowledgeAgent:
    def __init__(self):
        self.rules = load_rules()

    def analyze(self, visual_output, user_text=None):
        palette = visual_output["palette"]
        color_confidence = visual_output["color_confidence"]

        base_color = simple_color_name(palette[0])

        # --- Decision variables ---
        request_complexity = self._estimate_request_complexity(user_text)
        needs_external = self._decide_need_external(color_confidence, request_complexity)

        if needs_external:
            result = find_best_match([base_color], self.rules)
            retrieval_confidence = 1.0 if result["matches"] else 0.0
        else:
            result = {
                "base_color": base_color,
                "matches": ["white", "black"],  # simple fallback
                "style": "Basic matching without external rules."
            }
            retrieval_confidence = 0.5

        return {
            "base_color": result["base_color"],
            "matches": result["matches"],
            "style": result["style"],
            "used_external": needs_external,
            "retrieval_confidence": retrieval_confidence
        }

    def _estimate_request_complexity(self, user_text):
        if not user_text:
            return 0.2

        length = len(user_text.split())
        return min(length / 10, 1.0)

    def _decide_need_external(self, color_confidence, request_complexity):
        if request_complexity > 0.5:
            return True
        if color_confidence < 0.6:
            return True
        return False
