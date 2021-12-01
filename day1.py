from typing import List

INPUT_FILE = "input-day1.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    values = [int(x) for x in lines]
    count = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            count += 1
    print(count)
    return


def part2():
    lines = get_lines(INPUT_FILE)
    values = [int(x) for x in lines]
    count = 0
    prev_sum = sum(values[0:3])
    for i in range(3, len(values)):
        new_sum = prev_sum + values[i] - values[i-3]
        if new_sum > prev_sum:
            count += 1
        prev_sum = new_sum
    print(count)
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
