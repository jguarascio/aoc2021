from typing import List

INPUT_FILE = "input-day7.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def get_fuel(pos_list, pos):
    fuel = 0
    for i in pos_list:
        fuel += abs(i - pos)
    return fuel


def get_fuel2(pos_list, pos):
    fuel = 0
    for i in pos_list:
        d = abs(i - pos)
        cost = d*(d+1)//2
        fuel += cost
    return fuel


def part1():
    lines = get_lines(INPUT_FILE)
    pos_list = [int(x) for x in lines[0].split(",")]
    pos = 0
    min_fuel = float("inf")
    for i in range(max(pos_list)+1):
        fuel = get_fuel(pos_list, i)
        if fuel < min_fuel:
            min_fuel = fuel
            pos = i
    print(f"{pos=} {min_fuel=}")
    return


def part2():
    lines = get_lines(INPUT_FILE)
    pos_list = [int(x) for x in lines[0].split(",")]
    pos = 0
    min_fuel = float("inf")
    for i in range(max(pos_list)+1):
        fuel = get_fuel2(pos_list, i)
        if fuel < min_fuel:
            min_fuel = fuel
            pos = i
    print(f"{pos=} {min_fuel=}")
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
