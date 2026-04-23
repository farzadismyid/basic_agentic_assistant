from src.utils.image_io import load_image
from src.utils.color_analysis import extract_dominant_colors


def test_color_extraction():
    image = load_image("data/sample_images/test.jpg")
    colors = extract_dominant_colors(image, k=3)

    assert len(colors) == 3
