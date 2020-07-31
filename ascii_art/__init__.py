from PIL import Image, ImageDraw, ImageFont


def weigh(c, font):
    """Find and return density of dark pixels in the given character"""
    w, h = (6, 11)
    fw, fh = font.getsize(c)
    im = Image.new('L', (fw, fh))
    draw = ImageDraw.Draw(im)
    draw.text(((w - fw)/2, (h - fh)/2), c, 255, font=font)
    n = len([p for p in im.getdata() if p > 0])
    return n / (w * h)


def weigh_chars(chars, font, invert: bool, normalize: bool):
    weighted_chars = dict()
    for c in chars:
        w = weigh(c, font)
        weighted_chars[c] = w if invert else 1 - w

    if normalize:
        cmax = max(weighted_chars.values())
        cmin = min(weighted_chars.values())
        for c in weighted_chars.keys():
            weighted_chars[c] = (weighted_chars[c] - cmin) / (cmax - cmin)

    return weighted_chars


def find_char(pixel, weighted_chars):
    """Find and return character from dict with similar darkness to image pixel"""
    return min(weighted_chars.keys(), key=lambda c: abs(pixel - weighted_chars[c]))


def image_to_ascii(image, width=None, height=None, chars=' .\',:;+*?%S#@', font=None, invert=False, normalize=False):
    """Convert image to ASCII chars"""
    img_w, img_h = image.size
    if width and not height:
        height = int(img_h * (width / img_w))
    elif height and not width:
        width = int(img_w * (height / img_h))

    image = image.resize((width, height)).convert('L')

    if not font:
        font = ImageFont.load_default()
    elif isinstance(font, str):
        font = ImageFont.truetype(font)

    weighted_chars = weigh_chars(chars, font, invert, normalize)

    pixels = image.load()
    ascii_art = ''

    for i in range(height):
        for j in range(width):
            ascii_art += find_char(pixels[j, i] / 255, weighted_chars)
            if j == width - 1:
                ascii_art += '\n'

    return ascii_art
