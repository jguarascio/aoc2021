from typing import List
from statistics import median

INPUT_FILE = "input-day10.txt"

CHUNK_MARKERS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    ERROR_SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    lines = get_lines(INPUT_FILE)
    errors = dict()
    for line in lines:
        chunks = list()
        for c in line:
            if c in CHUNK_MARKERS.values():
                chunks.append(c)
            elif c in CHUNK_MARKERS.keys():
                opener = CHUNK_MARKERS[c]
                if chunks[len(chunks)-1] == opener:
                    chunks.pop()
                else:
                    errors[c] = errors.get(c, 0) + 1
                    break
    score = 0
    for error in errors:
        score += ERROR_SCORES[error] * errors[error]
    print(score)

    return


def part2():
    VALUES = ['(', '[', '{', '<']
    lines = get_lines(INPUT_FILE)
    scores = list()
    for line in lines:
        discard = False
        chunks = list()
        for c in line:
            if c in CHUNK_MARKERS.values():
                chunks.append(c)
            elif c in CHUNK_MARKERS.keys():
                opener = CHUNK_MARKERS[c]
                if chunks[-1] == opener:
                    chunks.pop()
                else:
                    discard = True
                    break
        
        # calculate score
        if not discard and len(chunks) > 0:
            score = 0
            chunks.reverse()
            for i in chunks:
                score *= 5
                score += VALUES.index(i) + 1
            scores.append(score)

    print(median(scores))
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
