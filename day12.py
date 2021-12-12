from typing import List
from collections import defaultdict
from pprint import pprint

INPUT_FILE = "input-day12.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_paths_part1(graph, start, end, visited, path, path_list):
    visited[start] = True
    path.append(start)
    if start == end:
        path_list.append(",".join(path))
    else:
        for neighbor in graph[start]:
            if neighbor == neighbor.upper() or visited[neighbor] == False:
                get_paths_part1(graph, neighbor, end, visited, path, path_list)
    path.pop()
    visited[start] = False

    return

def get_paths_part2(graph, start, end, visited, path, path_list):
    visited[start] += 1
    path.append(start)
    if start == end:
        path_list.append(",".join(path))
    else:
        for neighbor in graph[start]:
            if neighbor == neighbor.upper():
                get_paths_part2(graph, neighbor, end, visited, path, path_list)
            elif neighbor in ('start','end'):
                if visited[neighbor] == 0:
                    get_paths_part2(graph, neighbor, end, visited, path, path_list)
            elif neighbor == neighbor.lower():
                if visited[neighbor] == 0:
                    get_paths_part2(graph, neighbor, end, visited, path, path_list)
                elif visited[neighbor] == 1:
                    get_paths_part2(graph, neighbor, end, visited, path, path_list)
                    for node in graph:
                        if node == node.lower() and node != 'end':
                            visited[node] += 1
                    print(visited)
                    input()
    path.pop()
    visited[start] -= 1

    return


def make_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        parts = line.split("-")
        start = parts[0]
        end = parts[1]
        graph[start].append(end)
        graph[end].append(start)
    return graph

def part1():
    lines = get_lines(INPUT_FILE)
    graph = make_graph(lines)

    path_list = []
    path = []
    visited = defaultdict(lambda: False)
    get_paths_part1(graph, 'start', 'end', visited, path, path_list)
    print(len(path_list))

    return


def part2():
    lines = get_lines(INPUT_FILE)
    graph = make_graph(lines)

    path_list = []
    path = []
    visited = defaultdict(lambda: 0)
    get_paths_part2(graph, 'start', 'end', visited, path, path_list)
    print(len(path_list))
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
