def simple_color_name(hex_color):
    hex_color = hex_color.lower()

    if hex_color.startswith("#0") or hex_color.startswith("#1"):
        return "black"
    if "ff" in hex_color and "ff" in hex_color[3:]:
        return "white"
    if "00" in hex_color[:3]:
        return "blue"
    if "8" in hex_color:
        return "brown"

    return "blue"  # fallback
