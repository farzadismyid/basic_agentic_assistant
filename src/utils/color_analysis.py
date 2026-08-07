import numpy as np
from sklearn.cluster import KMeans


def extract_dominant_colors(image, k=3):
    image = image.resize((150, 150))  # speed
    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(pixels)

