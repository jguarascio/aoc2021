from typing import List
from statistics import median

INPUT_FILE = "input-day10.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


chunk_markers = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<',
}

error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part1():
    lines = get_lines(INPUT_FILE)
    errors = dict()
    for line in lines:
        chunks = list()
        for i in range(len(line)):
            if line[i] in chunk_markers.values():
                opener = line[i]
                chunks.append(opener)
            elif line[i] in chunk_markers.keys():
                opener = chunk_markers[line[i]]
                if chunks[len(chunks)-1] == opener:
                    chunks.pop()
                else:
                    errors[line[i]] = errors.get(line[i], 0) + 1
                    break
    score = 0
    for error in errors:
        score += error_scores[error] * errors[error]
    print(score)

    return


def part2():
    lines = get_lines(INPUT_FILE)
    scores = list()
    for line in lines:
        discard = False
        chunks = list()
        for i in range(len(line)):
            if line[i] in chunk_markers.values():
                opener = line[i]
                chunks.append(opener)
            elif line[i] in chunk_markers.keys():
                opener = chunk_markers[line[i]]
                if chunks[len(chunks)-1] == opener:
                    chunks.pop()
                else:
                    discard = True
                    break
        if not discard and len(chunks) > 0:
            # calculate score
            score = 0
            values = ['(','[', '{','<']
            for i in range(len(chunks)-1, -1, -1):
                score *= 5
                score += values.index(chunks[i]) + 1
            scores.append(score)
    
    print(median(scores))
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
