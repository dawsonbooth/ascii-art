import argparse


def main():

    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('pos', type=str,
                        help='The positional arg')
    parser.add_argument('-f', '--flag1', type=int, default=0,
                        help='First page of scraping')
    parser.add_argument('-p', '--progress', type=bool, default=True,
                        help='Display progress')
    parser.add_argument('-v', '--verbose', type=bool, default=False,
                        help='Display error statements')

    args = parser.parse_args()

    try:
        print()
    except KeyboardInterrupt:
        print("Terminated.")


if __name__ == '__main__':
    main()
