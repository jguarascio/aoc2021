from typing import List

INPUT_FILE = "input-day3.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    input_size = len(lines)
    item_size = len(lines[0])
    counts = [0 for x in range(item_size)]
    for line in lines:
        for x in range(item_size):
            counts[x] += int(line[x])

    gamma = 0
    epsilon = 0
    for x in range(item_size-1, -1, -1):
        if counts[x] > input_size/2:
            gamma += 2**(item_size-1-x)
        else:
            epsilon += 2**(item_size-1-x)

    print(f"{gamma=} {epsilon=} product={gamma*epsilon}")

    return


def part2():
    lines = get_lines(INPUT_FILE)
    input_size = len(lines)
    item_size = len(lines[0])

    new_list = lines
    for x in range(item_size):
        count = 0
        temp_list = new_list
        input_size = len(temp_list)
        for line in temp_list:
            count += int(line[x])
        new_list = list()
        for line in temp_list:
            if count >= input_size/2 and line[x] == '1':
                new_list.append(line)
            elif count < input_size/2 and line[x] == '0':
                new_list.append(line)
        if len(new_list) == 1:
            break

    o2 = int(new_list[0], 2)

    new_list = lines
    for x in range(item_size):
        count = 0
        temp_list = new_list
        input_size = len(temp_list)
        for line in temp_list:
            count += int(line[x])
        new_list = list()
        for line in temp_list:
            if count >= input_size/2 and line[x] == '0':
                new_list.append(line)
            elif count < input_size/2 and line[x] == '1':
                new_list.append(line)
        if len(new_list) == 1:
            break

    co2 = int(new_list[0], 2)

    print(f"{o2=} {co2=} product={o2*co2}")
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
