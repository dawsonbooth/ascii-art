import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("pos", type=str, help="The positional arg")
    parser.add_argument("-f", "--flag1", type=int, default=0, help="This is the first flag")
    parser.add_argument("-p", "--progress", type=bool, default=True, help="Display progress")
    parser.add_argument("-v", "--verbose", type=bool, default=False, help="Display error statements")

    args = parser.parse_args()

    try:
        print(args.pos)
        print(f"The first flag is {args.flag1}")
        if args.verbose:
            print("Some more info")
    except KeyboardInterrupt:
        print("Terminated.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
