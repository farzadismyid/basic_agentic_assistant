import numpy as np
from sklearn.cluster import KMeans


def extract_dominant_colors(image, k=3):
    image = image.resize((150, 150))  # speed
    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    return colors


def rgb_to_hex(color):
    return '#%02x%02x%02x' % tuple(color)


def get_palette_hex(colors):
    return [rgb_to_hex(c) for c in colors]
