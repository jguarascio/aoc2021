from typing import List, Dict
from collections import defaultdict
from operator import itemgetter

INPUT_FILE = "input-day14.txt"


def get_lines(filename: str) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def get_rules(lines: List) -> Dict:
    rules = dict()
    for line in lines[2:]:
        parts = line.split(" -> ")
        rep = parts[0][0] + parts[1] + parts[0][1]
        rules[parts[0]] = rep
    return rules


def run_rules(template: str, rules: List, steps: int) -> str:

    # Set up dictionary
    pairs = defaultdict(lambda: 0)
    for i in range(len(template)-1):
        pair = template[i:i+2]
        pairs[pair] += 1
    
    # Run rules
    for step in range(steps):
        new_dict = defaultdict(lambda: 0)
        for pair in pairs:
            if pair in rules.keys():
                new = rules[pair]
                new_dict[new[0:2]] += pairs[pair]
                new_dict[new[1:3]] += pairs[pair]
        pairs = new_dict

    # Add entry for last character in template
    pairs[template[-1]] = 1

    return pairs


def get_counts(d: Dict) -> List:
    counts = dict()
    for key, value in d.items():
        counts[key[0]] = counts.get(key[0], 0) + value
    return sorted(counts.items(), key=itemgetter(1), reverse=True)


def part1():
    lines = get_lines(INPUT_FILE)
    template = lines[0]
    rules = get_rules(lines)
    result = run_rules(template, rules, 10)
    counts = get_counts(result)
    most_common = counts[0][1]
    least_common = counts[-1][1]
    print(most_common-least_common)
    return


def part2():
    lines = get_lines(INPUT_FILE)
    template = lines[0]
    rules = get_rules(lines)
    result = run_rules(template, rules, 40)
    counts = get_counts(result)
    most_common = counts[0][1]
    least_common = counts[-1][1]
    print(most_common-least_common)
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
