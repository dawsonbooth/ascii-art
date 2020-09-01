import argparse

from PIL import Image

from . import image_to_ascii


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
    parser.add_argument('--chars', type=str, default=' .\',:;+*?%S#@',
                        help='String containing characters to be seen in ASCII art')
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

    # Generate ASCII art from image
    ascii_art = image_to_ascii(
        image, args.width, args.height, args.chars, args.font, args.invert, args.normalize)

    # Print to terminal
    if args.terminal:
        print(ascii_art)

    # Output ASCII art
    if args.output:
        with open(args.output, 'wb') as f:
            f.write(ascii_art.encode('utf-8'))
        print('\nASCII art saved to ' + args.output, end='\n\n')


if __name__ == '__main__':
    main()
