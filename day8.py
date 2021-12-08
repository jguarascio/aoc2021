from typing import List

INPUT_FILE = "input-day8.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = get_lines(INPUT_FILE)
    digits = list()
    for line in lines:
        parts = line.split("|")
        #inp = parts[0].split()
        output = parts[1].split()
        for digit in output:
            if len(digit) == 2:
                digits.append(1)
            if len(digit) == 3:
                digits.append(7)
            if len(digit) == 4:
                digits.append(4)
            if len(digit) == 7:
                digits.append(8)
    print(digits)
    print(len(digits))

    return


def part2():
    lines = get_lines(INPUT_FILE)
    digits = list()
    total = 0
    for line in lines:
        parts = line.split("|")
        inp = [set(digit) for digit in parts[0].split()]
        output = [set(digit) for digit in parts[1].split()]

        digits = dict()
        # Deduce: 1, 7, 4, 8
        for digit in inp:
            if len(digit) == 2:
                digits[1] = digit
            if len(digit) == 3:
                digits[7] = digit
            if len(digit) == 4:
                digits[4] = digit
            if len(digit) == 7:
                digits[8] = digit
        
        
        for digit in inp:
            # Deduce: 9, 6, 0
            if len(digit) == 6:
                if len(digit - digits[1]) == 5:
                    digits[6] = digit
                elif len(digit - digits[4]) == 2:
                    digits[9] = digit
                else:
                    digits[0] = digit
            # Deduce: 5, 2, 3
            if len(digit) == 5:
                if len(digit - (digits[4]-digits[1])) == 3:
                    digits[5] = digit
                elif len(digit - digits[1]) == 3:
                    digits[3] = digit
                else:
                    digits[2] = digit

        display = ""
        for digit in output:
            for item in digits:
                if digit == digits[item]:
                    display += str(item)
        total += int(display)
    
    print(total)

    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
