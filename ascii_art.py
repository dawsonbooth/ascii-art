import argparse

from PIL import Image
from utils import image_to_ascii
from weight import weigh_chars


def main(args):

    image = Image.open(args.image)

    output = args.output
    if output and not output.endswith('.txt'):
        output += '.txt'

    width, length = image.size
    if args.width and args.length:
        width = args.width
        length = args.length
    elif args.width and not args.length:
        length = int(length * (args.width / width))
        width = args.width
    elif args.length and not args.width:
        width = int(width * (args.length / length))
        length = args.length

    chars = args.chars if args.chars else ' .\',:;+*?%S#@'
    weighted_chars = weigh_chars(chars, args.invert, args.normalize)

    # Generate ASCII art from image
    ascii_art = image_to_ascii(image, width, length, weighted_chars)

    # Output ASCII art
    with open(output, 'wb') as f:
        f.write(ascii_art.encode('utf-8'))
    print('\nASCII art saved to ' + output, end='\n\n')

    # Print to console if small enough
    if width <= 150 and length <= 150:
        print(ascii_art)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Convert your favorite image into ASCII art')
    parser.add_argument('image', type=str,
                        help='Path to image from which ASCII art will be generated')
    parser.add_argument('output', type=str, help='Path to generated ASCII art')
    parser.add_argument('--width', type=int,
                        help='Character width of ASCII art')
    parser.add_argument('--height', type=int,
                        help='Character height of ASCII art')
    parser.add_argument('--chars', type=str,
                        help='Path to characters to be seen in ASCII art')
    parser.add_argument('-i', '--invert', type=bool, default=False,
                        help='Whether the ASCII output color is inverted')
    parser.add_argument('-n', '--normalize', type=bool, default=True,
                        help='Whether the weights of the provided ASCII characters are normalized')
    args = parser.parse_args()

    # Run program
    main(args)
