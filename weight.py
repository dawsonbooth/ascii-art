from PIL import Image, ImageDraw


def weigh(c, font):
    """Find and return density of dark pixels in the given character"""
    w, h = (6, 11)
    fw, fh = font.getsize(c)
    im = Image.new('L', (fw, fh))
    draw = ImageDraw.Draw(im)
    draw.text(((w - fw)/2, (h - fh)/2), c, 255, font=font)
    n = len([p for p in im.getdata() if p > 5])
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
