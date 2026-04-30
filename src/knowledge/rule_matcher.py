def find_best_match(detected_colors, rules):
    # naive approach: pick first detected color
    base_color = detected_colors[0].lower()

    if base_color in rules:
        return {
            "base_color": base_color,
            "matches": rules[base_color]["matches"],
            "style": rules[base_color]["style"]
        }

    return {
        "base_color": base_color,
        "matches": [],
        "style": "No rule found for this color."
    }
