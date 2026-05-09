# src/agents/visual_agent.py

from src.utils.color_analysis import extract_dominant_colors, get_palette_hex
from src.utils.captioning import generate_caption


class VisualAgent:
    def __init__(self):
        pass

    def analyze(self, image, image_path=None):
        colors = extract_dominant_colors(image, k=3)
        palette = get_palette_hex(colors)

        color_confidence = self._estimate_color_confidence(colors)
        image_quality = self._estimate_image_quality(image)

        needs_caption = self._decide_caption_need(
            color_confidence,
            image_quality
        )

        caption = None

        if needs_caption and image_path:
            caption = generate_caption(image_path)

        return {
            "palette": palette,
            "color_confidence": color_confidence,
            "image_quality": image_quality,
            "needs_caption": needs_caption,
            "caption": caption
        }

    def _estimate_color_confidence(self, colors):
        return len(colors) / 3

    def _estimate_image_quality(self, image):
        width, height = image.size
        return min(width, height) / 300

    def _decide_caption_need(self, color_confidence, image_quality):
        if color_confidence < 0.5:
            return True

        if image_quality < 0.5:
            return True

        return False
