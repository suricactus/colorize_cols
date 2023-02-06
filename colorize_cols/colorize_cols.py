#!/usr/bin/env -S python3 -u
"""Convert a TSV to colored and well formated output for each column.

usage: colorize [-h] [-s SEPARATORS] [-o OUTPUT_SEPARATOR] [file]

positional arguments:
  file                  File to be colorized. Default: STDIN

options:
  -h, --help            show this help message and exit
  -s SEPARATORS, --separators SEPARATORS
                        Separators delimited by a comma. Default: \t
  -o OUTPUT_SEPARATOR, --output-separator OUTPUT_SEPARATOR
                        Output separator. Default: \t
"""

__author__ = "Ivan Ivanov"
__copyright__ = "Copyright 2022, Suricactus LTD"
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "Ivan Ivanov"
__email__ = "ivan.ivanov@suricactus.com"


import re
import sys
from typing import Dict, List

MIN_NUMERIC_WIDTH = 7

reset_color = "\033[0m"
colors = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # purple
    "\033[96m",  # cyan
]
colors_count = len(colors)


def colorize_line(
    line: str, separators: List[str], output_separator: str, sizes: Dict[int, int]
) -> str:
    separators = [re.escape(s) for s in separators]
    cols = re.split("|".join(separators), line)
    cols_count = len(cols)
    row = ""

    for col_idx, col in enumerate(cols):
        sizes[col_idx] = max(len(col), sizes.get(col_idx, 0))
        # print(col_idx, sizes[col_idx], col)

        row += reset_color
        row += colors[col_idx % colors_count]

        # add tab split if not last column
        if col_idx < cols_count - 1:
            if re.match(r"^\d+(\.\d+)?$", col):
                row += col.rjust(max(sizes[col_idx], MIN_NUMERIC_WIDTH), " ")
            else:
                row += col.ljust(sizes[col_idx], " ")

            row += output_separator
        else:
            row += col

        row += reset_color

    return row


def colorize(file: str, separators: str, output_separator: str) -> None:
    separators_str = separators
    separators = []

    if separators_str == ",":
        separators = [","]
    else:
        if ",," in separators_str:
            separators_str = separators_str.replace(",,", "")
            separators.append(",")

        separators += separators_str.split(",")

    sizes = {}

    for line in file:
        colorized_line = colorize_line(line, separators, output_separator, sizes)
        print(colorized_line, end="", flush=True)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert a TSV to colored and well formated output for each column."
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="File to be colorized. Default: STDIN",
    )
    parser.add_argument(
        "-s",
        "--separators",
        help="Separators delimited by a comma. Default: \\t",
        default="\t",
    )
    parser.add_argument(
        "-o",
        "--output-separator",
        help="Output separator. Default: \\t",
        default="\t",
    )
    args = parser.parse_args()

    colorize(
        args.file, separators=args.separators, output_separator=args.output_separator
    )


if __name__ == "__main__":
    main()
