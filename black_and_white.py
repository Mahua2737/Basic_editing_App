from PIL import ImageOps


def apply_black_and_white(image, intensity):
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image.point(lambda x: 0 if x < intensity else 255)
