import argparse

from PIL import Image
from image_ops import image_to_ascii
from weigh import weight

# Parse arguments
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('image', type=str, help='Path to image from which ASCII art will be generated')
parser.add_argument('output', type=str, help='Path to generated ASCII art')
parser.add_argument('-w', '--width', type=int, help='Character width of ASCII art')
parser.add_argument('-h', '--height', type=int, help='Character height of ASCII art')
parser.add_argument('-c', '--chars', type=str, help='Path to characters to be seen in ASCII art')
parser.add_argument('-i', '--invert', type=bool, help='Whether the ASCII output color is inverted')

args = parser.parse_args()

# Main function
def main():

    # Image
    image = Image.open(args.image)

    # Output
    output = args.output
    if not output.endswith('.txt'):
        output += '.txt'

    # Width and Height
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

    # Chars
    if args.chars:
        with open(args.chars, 'r') as f:
            chars = f.read().replace('\n', '')
    else:
        chars = ' .\',:;+*?%S#@'

    weighted_chars = dict()
    max_weight = 0
    for c in chars:
        w =  weight(c)
        if args.invert:
            w = 1 - w
        if w > max_weight:
            max_weight = w
        weighted_chars[c] = w

    for c in weighted_chars.keys():
        weighted_chars[c] *= (1 / max_weight)

    # Generate ASCII art from image
    ascii_art = image_to_ascii(image, width, height, weighted_chars)

    # Output ASCII art
    with open(output, 'wb') as f:
        f.write(ascii_art.encode('utf-8'))
    print('\nASCII art saved to ' + output, end='\n\n')

    # Print to console if small enough
    if width <= 150 and height <= 150:
        print(ascii_art)

if __name__ == '__main__':
    main()
