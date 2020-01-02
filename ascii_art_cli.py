import argparse

from PIL import Image, ImageDraw, ImageFont


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


def main():
    """ASCII art generator with multiple customization parameters"""
    parser = argparse.ArgumentParser(
        description='Convert your favorite image into ASCII art')
    parser.add_argument('input', type=str,
                        help='Path to image from which ASCII art will be generated')
    parser.add_argument('--output', type=str, default=None,
                        help='Path to output generated ASCII art')
    parser.add_argument('--width', type=int,
                        help='Character width of ASCII art')
    parser.add_argument('--height', type=int,
                        help='Character height of ASCII art')
    parser.add_argument('--chars', type=str,
                        help='Path to characters to be seen in ASCII art')
    parser.add_argument('--font', type=str,
                        help='Font for calculating the character weights')
    parser.add_argument('--invert', action='store_true',
                        help='Whether the ASCII output color is inverted')
    parser.add_argument('--normalize', action='store_true',
                        help='Whether the weights of the provided ASCII characters are normalized')
    parser.add_argument('--terminal', action='store_true',
                        help='Whether to output to the terminal')
    args = parser.parse_args()

    image = Image.open(args.input)

    width, height = image.size
    if args.width and args.height:
        width = args.width
        height = args.height
    elif args.width and not args.height:
        height = int(height * (args.width / width))
        width = args.width
    elif args.height and not args.width:
        width = int(width * (args.height / height))
        height = args.height

    if args.chars:
        with open(args.chars, 'r') as f:
            chars = f.read().replace('\n', '')
    else:
        chars = ' .\',:;+*?%S#@'

    font = ImageFont.truetype(
        args.font) if args.font else ImageFont.load_default()

    weighted_chars = weigh_chars(chars, font, args.invert, args.normalize)

    # Generate ASCII art from image
    ascii_art = image_to_ascii(image, width, height, weighted_chars)

    # Print to terminal
    if args.terminal:
        print(ascii_art)

    # Output ASCII art
    if args.output:
        with open(args.output, 'wb') as f:
            f.write(ascii_art.encode('utf-8'))
        print('\nASCII art saved to ' + args.output, end='\n\n')
