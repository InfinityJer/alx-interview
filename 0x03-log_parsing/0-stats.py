#!/usr/bin/python3
import sys
import re


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, status_codes):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) -
    \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')
    match = pattern.match(line)
    if match:
        ip, date, status_code, file_size = match.groups()
        return int(status_code), int(file_size)
    else:
        return None, None


def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line.strip(), status_codes)

            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code]
                = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle Ctrl+C
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
