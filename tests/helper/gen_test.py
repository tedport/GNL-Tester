import argparse
import os
import re
import sys


def bytes_literal(data: bytes) -> str:
    r = repr(data)
    if r.startswith("b'") and r.endswith("'") and '"' not in r[2:-1]:
        return 'b"' + r[2:-1] + '"'
    return r


def split_lines(data: bytes) -> list[bytes]:
    lines, start = [], 0
    for i, b in enumerate(data):
        if b == 0x0A:
            lines.append(data[start : i + 1])
            start = i + 1
    if start < len(data):
        lines.append(data[start:])
    return lines


def func_name_from(path: str) -> str:
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r"\W", "_", base)
    if not base or base[0].isdigit():
        base = "_" + base
    return f"test_{base}"


def gen_test(path: str, func_name: str | None = None) -> str:
    with open(path, "rb") as f:
        content = f.read()

    lines = split_lines(content)
    fname = func_name or func_name_from(path)
    basename = os.path.basename(path)

    parts = [
        f"def {fname}(lib):",
        f'    with open_gnl_file("{basename}") as fd:',
    ]

    if not lines:
        parts.append("        assert lib.get_next_line(fd) == ffi.NULL")
    else:
        for line in lines:
            lit = bytes_literal(line)
            single = f"        assert ffi.string(lib.get_next_line(fd)) == {lit}"
            if len(single) <= 100:
                parts.append(single)
            else:
                parts.append("        assert (")
                parts.append("            ffi.string(lib.get_next_line(fd))")
                parts.append(f"            == {lit}")
                parts.append("        )")
        parts.append("        assert lib.get_next_line(fd) == ffi.NULL")

    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate get_next_line pytest tests from text files."
    )
    ap.add_argument("files", nargs="+", help="input files")
    ap.add_argument("-o", "--output", help="output file (default: stdout)")
    ap.add_argument(
        "--header",
        default=None,
        help="custom header to prepend (default: minimal imports)",
    )
    ap.add_argument(
        "--no-header", action="store_true", help="do not prepend any header"
    )
    args = ap.parse_args()

    if args.no_header:
        header = ""
    elif args.header is not None:
        header = args.header + "\n\n"
    else:
        header = (
            '"""Auto-generated tests for get_next_line."""\n'
            "import ffi\n"
            "from conftest import open_gnl_file  # adjust import path as needed\n"
            "\n\n"
        )

    used, bodies = set(), []
    for p in args.files:
        base_name = func_name_from(p)
        candidate = base_name
        n = 2
        while candidate in used:
            candidate = f"{base_name}_{n}"
            n += 1
        used.add(candidate)
        bodies.append(gen_test(p, func_name=candidate))

    body = "\n\n\n".join(bodies) + "\n"
    output = header + body

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
