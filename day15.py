from typing import List
from pprint import pprint
from queue import PriorityQueue

INPUT_FILE = "input-day15.txt"

DELTA = [[-1, 0],   # go up
         [0, -1],   # go left
         [1, 0],    # go down
         [0, 1]]    # go right

DELTA_NAME = ['^', '<', 'v', '>']

def get_lines(filename: str) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    
    grid = [[int(x) for x in line] for line in lines]
    #pprint(grid)
    
    rows = len(grid)
    cols = len(grid[0])

    visited = [[0 for row in range(rows)] for col in range(cols)]
    
    
    # intialize cost matrix
    cost = [[float('inf') for row in range(rows)] for col in range(cols)]
    cost[0][0] = 0

    # initialize queue with starting point
    pq = PriorityQueue()
    pq.put((0, 0, 0))
    
    while not pq.empty():
        (dist, r, c) = pq.get()
        visited[r][c] = 1

        for d in range(len(DELTA)):
            nr = r + DELTA[d][0]
            nc = c + DELTA[d][1]
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and visited[nr][nc] == 0:
                old_cost = cost[nr][nc]
                new_cost = cost[r][c] + grid[nr][nc]
                if new_cost < old_cost:
                    pq.put((new_cost, nr, nc))
                    cost[nr][nc] = new_cost

    #pprint(cost)

    # Print cost to reach goal node
    print(cost[rows-1][cols-1])

    return


def part2():
    lines = get_lines(INPUT_FILE)
    grid = [[int(x) for x in line] for line in lines]
    
    rsize = len(grid)
    csize = len(grid[0]) 
    rows = len(grid)*5
    cols = len(grid[0])*5
    visited = [[0 for row in range(rows)] for col in range(cols)]
    
    
    # intialize cost matrix
    cost = [[float('inf') for row in range(rows)] for col in range(cols)]
    cost[0][0] = 0

    # initialize queue with starting point
    pq = PriorityQueue()
    pq.put((0, 0, 0))
    
    while not pq.empty():
        (dist, r, c) = pq.get()
        visited[r][c] = 1

        for d in range(len(DELTA)):
            nr = r + DELTA[d][0]
            nc = c + DELTA[d][1]
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and visited[nr][nc] == 0:
                cell_cost = (grid[nr % rsize][nc % csize] + nr // rsize + nc // csize)
                cell_cost = cell_cost % 10 + 1 if cell_cost > 9 else cell_cost
                old_cost = cost[nr][nc]
                new_cost = cost[r][c] + cell_cost
                if new_cost < old_cost:
                    pq.put((new_cost, nr, nc))
                    cost[nr][nc] = new_cost

    # Print cost to reach goal node
    print(cost[rows-1][cols-1])

    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
