from typing import List, Dict
from pprint import pprint
from math import ceil
import json

INPUT_FILE = "input-day18.txt"


def get_lines(filename: str) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def reduce(my_list: List) -> List:
    result = my_list
    change = True
    while change:
        change, result = explode(result)
        print(result)
        if change: continue
        change, result = split(result)
        print(result)
    return result

def add_left(item, carry):
    if carry is None:
        return item
    if isinstance(item, int):
        return item + carry
    return [add_left(item[0], carry), item[1]]

def add_right(item, carry):
    if carry is None:
        return item
    if isinstance(item, int):
        return item + carry
    return [item[0], add_right(item[0], carry)]


def explode(item, depth = 0):
    print(f"{item=}, {depth=}")
    if isinstance(item, List):
        if depth == 4:
            return True, 0

        left, right = item

        change, result = explode(left, depth+1)

        if change:
            carry = left[1]
            return True, [result, right]
        
        change, result = explode(right, depth+1)
        if change:
            return True, [left, result]

    return False, item


def split(item):
    if isinstance(item, int):
        if item >= 10:
            return True, [item//2, ceil(item/2)]
        else:
            return False, item
    else:
        a, b = item
        change, a = split(a)
        if change:
            return True, [a,b]
        change, b = split(b)
        return change, [a,b]


def magnitude(item) -> int:
    if isinstance(item, int):
        return item
    elif isinstance(item, List):
        return 3*magnitude(item[0]) + 2*magnitude(item[1])


def test_magnitude():
    assert magnitude(json.loads("[[1,2],[[3,4],5]]")) == 143
    assert magnitude(json.loads("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")) == 1384
    assert magnitude(json.loads("[[[[1,1],[2,2]],[3,3]],[4,4]]")) == 445
    assert magnitude(json.loads("[[[[3,0],[5,3]],[4,4]],[5,5]]")) == 791
    assert magnitude(json.loads("[[[[5,0],[7,4]],[5,5]],[6,6]]")) == 1137
    assert magnitude(json.loads(
        "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")) == 3488


def test_reduce():
    # test = json.loads("[[[[[9,8],1],2],3],4]")
    # result = reduce(test, 0, dict())
    # print(result)

    # test = json.loads("[7,[6,[5,[4,[3,2]]]]]")
    # result = reduce(test, 0, dict())
    # print(result)

    # test = json.loads("[[6,[5,[4,[3,2]]]],1]")
    # result = reduce(test, 0, dict())
    # print(result)

    # test = json.loads("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    # result = reduce(test, 0, dict())
    # print(result)

    test = json.loads("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    result = reduce(test)
    print(result)


def add_lists(list1: List, list2: List) -> List:
    result = [list1, list2]
    result = reduce(result)
    return result


def part1():
    lines = get_lines(INPUT_FILE)

    for i, line in enumerate(lines):
        if i == 0:
            result = json.loads(line)
        else:
            result = add_lists(result, json.loads(line))

    print(magnitude(result))

    return


def part2():
    lines = get_lines(INPUT_FILE)
    return


def main():
    # test_magnitude()
    test_reduce()
    # part1()
    # part2()


if __name__ == "__main__":
    main()
