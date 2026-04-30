import json


def load_rules(path="data/fashion_rules.json"):
    with open(path, "r") as f:
        return json.load(f)
