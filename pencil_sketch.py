from PIL import ImageOps, ImageFilter


def apply_pencil_sketch(image, intensity):
    grayscale_image = ImageOps.grayscale(image)
    blurred_image = grayscale_image.filter(ImageFilter.GaussianBlur(radius=intensity))
    inverted_image = ImageOps.invert(blurred_image)
    return inverted_image
