import argparse
import random
import sys


def generate_random_line(length: int) -> str:
    out = ""
    for _ in range(length):
        out += chr(random.randint(32, 126))
    return out

def generate_many_lines(line_amount, r : range):
    out = []
    for _ in range(line_amount):
        out.append(generate_random_line(random.randint(r.start, r.stop)))
    return out

def lines_list_to_str(l : list[str], newlines_in_between = 1):
    if not l:
        return ""
        
    out = ""
    for line_idx in range(len(l) - 1):
        out += l[line_idx]
        out += "\n"*newlines_in_between
    out += l[len(l) - 1]
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate random ASCII lines and print them to stdout."
    )
    parser.add_argument(
        "-n", "--lines",
        type=int,
        default=64,
        help="Number of random lines to generate (default: 64).",
    )
    parser.add_argument(
        "--min-len",
        type=int,
        default=64,
        dest="min_len",
        help="Minimum length of each generated line (default: 64).",
    )
    parser.add_argument(
        "--max-len",
        type=int,
        default=512,
        dest="max_len",
        help="Maximum length of each generated line (default: 512).",
    )
    parser.add_argument(
        "--nl-between",
        type=int,
        default=1,
        dest="nl_between",
        help="Number of newlines between each line (default: 1).",
    )

    args = parser.parse_args()

    if args.min_len > args.max_len:
        parser.error("--min-len must not be greater than --max-len")
    if args.lines < 0:
        parser.error("--lines must not be negative")
    if args.min_len < 0 or args.max_len < 0:
        parser.error("line lengths must not be negative")
    if args.nl_between < 0:
        parser.error("--nl-between must not be negative")

    sys.stdout.write(
        lines_list_to_str(
            generate_many_lines(args.lines, range(args.min_len, args.max_len)),
            args.nl_between
        )
    )