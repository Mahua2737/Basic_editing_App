from PIL import ImageFilter


def apply_blur_effect(image, intensity):
    return image.filter(ImageFilter.GaussianBlur(radius=intensity))
