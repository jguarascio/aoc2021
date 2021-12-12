from typing import List

INPUT_FILE = "input-day11.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def print_grid(grid):
    for r in grid:
        print("".join([str(c) for c in r]))
    return


def flash(octopuses, row, col):
    rows = len(octopuses)
    cols = len(octopuses[0])

    flash_count = 0
    if octopuses[row][col] == 10:
        flash_count = 1
        # Flash, update adjacent octopuses
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                nr = row + r
                nc = col + c
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and octopuses[nr][nc] < 10:
                    octopuses[nr][nc] += 1
                    flash_count += flash(octopuses, nr, nc)
    return flash_count

def part1():
    lines = get_lines(INPUT_FILE)
    octopuses = [[int(x) for x in line] for line in lines]

    rows = len(octopuses)
    cols = len(octopuses[0])

    STEPS = 100
    flash_count = 0
    for steps in range(STEPS):

        for i in range(rows):
            for j in range(cols):
                if octopuses[i][j] < 10:
                    octopuses[i][j] += 1
                    flash_count += flash(octopuses, i, j)
        for i in range(rows):
            for j in range(cols):
                if octopuses[i][j] == 10:
                    octopuses[i][j] = 0

    #print_grid(octopuses)
    print(flash_count)

    return


def part2():
    lines = get_lines(INPUT_FILE)
    octopuses = [[int(x) for x in line] for line in lines]

    rows = len(octopuses)
    cols = len(octopuses[0])

    total = -1
    flash_count = 0
    step_count = 0
    while total != 0:
        for i in range(rows):
            for j in range(cols):
                if octopuses[i][j] < 10:
                    octopuses[i][j] += 1
                    flash_count += flash(octopuses, i, j)
        total = 0
        for i in range(rows):
            for j in range(cols):
                if octopuses[i][j] == 10:
                    octopuses[i][j] = 0
                total += octopuses[i][j]
        step_count += 1

    print(step_count)
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
