from typing import List

INPUT_FILE = "input-day6.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    ITERATIONS = 80
    LIFE_SPAN = 6
    NEW_AGE = 8

    lines = get_lines(INPUT_FILE)
    fish_list = [int(x) for x in lines[0].split(",")]

    for i in range(ITERATIONS):
        num_fish = len(fish_list)
        for j in range(num_fish):
            if fish_list[j] == 0:
                fish_list[j] = LIFE_SPAN
                fish_list.append(NEW_AGE)
            else:
                fish_list[j] -= 1
        # print(fish_list)

    print(len(fish_list))

    return


def part2():
    ITERATIONS = 256
    LIFE_SPAN = 6
    NEW_AGE = 8

    lines = get_lines(INPUT_FILE)
    fish_list = [int(x) for x in lines[0].split(",")]

    fish_by_age = dict()
    for age in fish_list:
        fish_by_age[age] = fish_by_age.get(age, 0) + 1

    for i in range(ITERATIONS):
        new_ages = dict()
        for age in fish_by_age.keys():
            if age == 0:
                new_ages[LIFE_SPAN] = new_ages.get(LIFE_SPAN, 0) + fish_by_age[age]
                new_ages[NEW_AGE] = fish_by_age[age]
            else:
                new_ages[age - 1] = new_ages.get(age - 1, 0) + fish_by_age[age]
            fish_by_age[age] = 0
        fish_by_age = new_ages

    print(sum(fish_by_age.values()))

    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
