def find_char(p, weighted_chars):
    """Find and return character from list with similar darkness to image pixel"""
    p /= 255
    closest_c = next(iter(weighted_chars))
    for c in weighted_chars.keys():
        w = weighted_chars[c]
        if abs(p - w) < abs(p - weighted_chars[closest_c]):
            closest_c = c
    return closest_c


def image_to_ascii(image, width, height, weighted_chars):
    """Convert image to ASCII chars"""
    image = image.resize((width, height)).convert('L')

    pixels = image.load()
    ascii_art = ''

    for i in range(height):
        for j in range(width):
            ascii_art += find_char(pixels[j, i], weighted_chars)
            if j == width - 1:
                ascii_art += '\n'

    return ascii_art
