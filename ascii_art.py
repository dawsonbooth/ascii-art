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
    weighted_chars = weigh_chars(chars, args.invert)

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
    parser.add_argument('-w', '--width', type=int,
                        help='Character width of ASCII art')
    parser.add_argument('-l', '--length', type=int,
                        help='Character length of ASCII art')
    parser.add_argument('-c', '--chars', type=str,
                        help='Path to characters to be seen in ASCII art')
    parser.add_argument('-i', '--invert', type=bool,
                        help='Whether the ASCII output color is inverted')

    args = parser.parse_args()

    # Run program
    main(args)
