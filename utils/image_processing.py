import numpy as np

def calculate_image_variance(image):
    return np.var(image)

def normalize_image(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))