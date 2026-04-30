from src.knowledge.rule_loader import load_rules
from src.knowledge.rule_matcher import find_best_match


def test_rule_matching():
    rules = load_rules()
    result = find_best_match(["blue"], rules)

    assert "white" in result["matches"]
