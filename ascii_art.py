import argparse

from PIL import Image
from image_ops import image_to_ascii
from weight import weigh_chars


# Main function
def main(args):

    # Image
    image = Image.open(args.image)

    # Output
    output = args.output
    if not output.endswith('.txt'):
        output += '.txt'

    # Width and length
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

    # Chars
    if args.chars:
        with open(args.chars, 'r') as f:
            chars = f.read().replace('\n', '')
    else:
        chars = ' .\',:;+*?%S#@'

    weighted_chars = weigh_chars(chars)

    # Invert
    if args.invert:
        for c in weighted_chars.keys():
            weighted_chars[c] = 1 - weighted_chars[c]

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
    parser.add_argument(
        'image', type=str, help='Path to image from which ASCII art will be generated')
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
