from typing import List

INPUT_FILE = "input.txt"


def get_lines(filename: str) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    return


def part2():
    lines = get_lines(INPUT_FILE)
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
