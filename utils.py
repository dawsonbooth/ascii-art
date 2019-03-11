# Find char with similar darkness to image pixel
def find_char(p, weighted_chars):
    p /= 255
    closest_c = next(iter(weighted_chars))
    for c in weighted_chars.keys():
        w = weighted_chars[c]  # weight
        if abs(p - w) < abs(p - weighted_chars[closest_c]):
            closest_c = c
    return closest_c


# Convert image to ASCII chars
def image_to_ascii(image, width, length, weighted_chars):
    image = image.resize((width, length)).convert('L')

    pixels = image.load()
    ascii_art = ''

    for i in range(length):
        for j in range(width):
            ascii_art += find_char(pixels[j, i], weighted_chars)
            if j == width-1:
                ascii_art += '\n'

    return ascii_art
