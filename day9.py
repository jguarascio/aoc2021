from typing import List

INPUT_FILE = "input-day9.txt"

directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def get_grid(lines) -> List:
    grid = list()
    for line in lines:
        grid.append([int(x) for x in list(line)])
    return grid


def part1():
    lines = get_lines(INPUT_FILE)
    grid = get_grid(lines)
    rows = len(grid)
    cols = len(grid[0])
    low_points = list()
    for i in range(rows):
        for j in range(cols):
            smallest = True
            for d in directions:
                nr = i + d[0]
                nc = j + d[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[i][j] >= grid[nr][nc]:
                    smallest = False
            if smallest:
                low_points.append(grid[i][j])

    print(sum(low_points) + len(low_points))

    return


def bfs(grid, sr, sc) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for c in range(cols)] for r in range(rows)]
    queue = list()

    queue.append((sr, sc))
    visited[sr][sc] = 1

    size = 1
    while queue:
        start = queue.pop(0)
        for d in directions:
            nr = start[0] + d[0]
            nc = start[1] + d[1]
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] != 9 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                size += 1

    return size


def part2():
    lines = get_lines(INPUT_FILE)
    grid = get_grid(lines)
    rows = len(grid)
    cols = len(grid[0])

    basin_sizes = list()
    for i in range(rows):
        for j in range(cols):
            smallest = True
            for d in directions:
                nr = i + d[0]
                nc = j + d[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[i][j] >= grid[nr][nc]:
                    smallest = False
            if smallest:
                # from here find basin size
                basin_size = bfs(grid, i, j)
                basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
