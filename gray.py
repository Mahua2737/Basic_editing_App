from PIL import ImageOps


def apply_gray(image):
    return ImageOps.grayscale(image)
