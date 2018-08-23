# Find char with similar darkness to image pixel
def find_char(p, chars):
    n = 255/len(chars)

    sections = [n*i for i, v in enumerate(chars)]

    for i, s in enumerate(sections):
        if p < s:
            return chars[i-1]
    return chars[-1]

# Convert image to ASCII chars
def image_to_ascii(image, width, height, chars="M@%#*+=-:. "):
    image = image.resize((width, height)).convert('L')

    pixels = image.load()
    ascii_art = ''

    for i in range(height):
        for j in range(width):
            ascii_art += find_char(pixels[j, i], chars)
            if j == width-1:
                ascii_art += '\n'

    return ascii_art
