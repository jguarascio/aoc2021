from typing import List

INPUT_FILE = "input-day5.txt"
GRID_SIZE = 1000


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def add_line(grid, point1, point2):
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])

    x, y = x1, y1
    incx = 1 if x1 < x2 else -1
    incy = 1 if y1 < y2 else -1
    while True:
        grid[y][x] += 1
        if x == x2 and y == y2:
            break
        if x != x2:
            x += incx
        if y != y2:
            y += incy
        

    return


def print_grid(grid):
    for row in grid:
        print(row)
    return


def count_overlaps(grid):
    count = 0
    for y in grid:
        for x in y:
            if x >= 2:
                count += 1
    return count


def part1():
    lines = get_lines(INPUT_FILE)
    grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    for line in lines:
        end_points = line.replace(" ", "").split("->")
        point1 = end_points[0].split(",")
        point2 = end_points[1].split(",")
        if point1[0] == point2[0] or point1[1] == point2[1]:
            add_line(grid, point1, point2)

    count = count_overlaps(grid)
    print(f"{count=}")
    return


def part2():
    lines = get_lines(INPUT_FILE)
    grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    for line in lines:
        end_points = line.replace(" ", "").split("->")
        point1 = end_points[0].split(",")
        point2 = end_points[1].split(",")
        add_line(grid, point1, point2)

    count = count_overlaps(grid)
    print(f"{count=}")    
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
