from typing import List

INPUT_FILE = "input-day2.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    pos = 0
    depth = 0
    for line in lines:
        op = line.split()
        opcode = op[0]
        operand = int(op[1])
        if opcode == 'forward':
            pos += operand
        elif opcode == 'down':
            depth += operand
        elif opcode == 'up':
            depth -= operand
    print(f'{pos=} {depth=} product={pos*depth}')
    return


def part2():
    lines = get_lines(INPUT_FILE)
    pos = 0
    depth = 0
    aim = 0
    for line in lines:
        op = line.split()
        opcode = op[0]
        operand = int(op[1])
        if opcode == 'forward':
            pos += operand
            depth += aim * operand
        elif opcode == 'down':
            aim += operand
        elif opcode == 'up':
            aim -= operand
    print(f'{pos=} {depth=} {aim=} product={pos*depth}')
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
