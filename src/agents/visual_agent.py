from src.utils.color_analysis import extract_dominant_colors, get_palette_hex


class VisualAgent:
    def __init__(self):
        pass

    def analyze(self, image):
        colors = extract_dominant_colors(image, k=3)
        palette = get_palette_hex(colors)

        # --- Decision variables ---
        color_confidence = self._estimate_color_confidence(colors)
        image_quality = self._estimate_image_quality(image)

        needs_caption = self._decide_caption_need(color_confidence, image_quality)

        return {
            "palette": palette,
            "color_confidence": color_confidence,
            "image_quality": image_quality,
            "needs_caption": needs_caption
        }

    def _estimate_color_confidence(self, colors):
        # simple heuristic: variance between clusters
        return len(colors) / 3  # normalized (0 to 1)

    def _estimate_image_quality(self, image):
        # placeholder heuristic
        width, height = image.size
        return min(width, height) / 300  # normalize

    def _decide_caption_need(self, color_confidence, image_quality):
        if color_confidence < 0.5 or image_quality < 0.5:
            return True
        return False
