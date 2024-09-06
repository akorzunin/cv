#!/usr/bin/env python
import argparse
import sys


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Get input files")

    # Add positional arguments for file names
    parser.add_argument("files", nargs="+", help="One or more input file names")

    # Add optional arguments
    parser.add_argument(
        "-i",
        "--input_directory",
        default="./",
        help="Path to the input directory",
    )
    parser.add_argument(
        "-l",
        "--language_code",
        default="",
        help="Language code",
        nargs="?",
        const="",
    )

    # Parse the arguments
    args = parser.parse_args()

    for arg in args.files:
        print(f"./{args.input_directory}/{arg}{args.language_code}.md")


if __name__ == "__main__":
    main()
