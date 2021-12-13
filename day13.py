from typing import List
import re

INPUT_FILE = "input-day13.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def get_points(lines):
    points = []
    for line in lines:
        if ',' in line:
            parts = line.split(",")
            x = int(parts[0])
            y = int(parts[1])
            points.append((x, y))
    return points


def get_folds(lines):
    folds = []
    for line in lines:
        if line.startswith("fold"):
            fold = re.findall("[x|y]=\d*", line)[0].split("=")
            folds.append((fold[0], int(fold[1])))
    return folds


def part1():
    lines = get_lines(INPUT_FILE)
    points = get_points(lines)
    folds = get_folds(lines)

    for fold in folds:
        if fold[0] == 'x':
            for i, point in enumerate(points):
                if point[0] > fold[1]:
                    points[i] = (fold[1] - (point[0] - fold[1]), point[1])
                pass
        elif fold[0] == 'y':
            for i, point in enumerate(points):
                if point[1] > fold[1]:
                    points[i] = (point[0], fold[1] - (point[1] - fold[1]))
        break

    point_count = len(set(points))

    print(point_count)

    return


def print_points(points):
    maxx = 0
    maxy = 0
    for point in points:
        maxx = max(int(point[0]), maxx)
        maxy = max(int(point[1]), maxy)

    page = [['.' for r in range(maxx+1)] for c in range(maxy+1)]

    for point in points:
        page[point[1]][point[0]] = '#'

    for r in page:
        print("".join(r))

    return


def part2():
    lines = get_lines(INPUT_FILE)
    points = get_points(lines)
    folds = get_folds(lines)

    for fold in folds:
        if fold[0] == 'x':
            for i, point in enumerate(points):
                if point[0] > fold[1]:
                    points[i] = (fold[1] - (point[0] - fold[1]), point[1])
                pass
        elif fold[0] == 'y':
            for i, point in enumerate(points):
                if point[1] > fold[1]:
                    points[i] = (point[0], fold[1] - (point[1] - fold[1]))

    print_points(points)

    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
