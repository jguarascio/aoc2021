from typing import List

INPUT_FILE = "input-day4.txt"


def get_lines(filename) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def get_boards(lines):
    boards = list()
    board = list()
    for i in range(2, len(lines)+1):
        if i == len(lines) or lines[i] == "":
            boards.append(board)
            board = list()
        else:
            board.append(lines[i].split())

    return boards


def update_board(board, num):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == num:
                board[i][j] = '-1'
    return board


def bingo(board):
    # Check rows
    for row in board:
        if sum([int(item) for item in row]) == -5:
            return True

    # Check columns
    for i in range(len(board[0])):
        total = 0
        for row in board:
            total += int(row[i])
        if total == -5:
            return True

    return False


def sum_board(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '-1':
                total += int(board[i][j])
    return total


def part1():
    lines = get_lines(INPUT_FILE)
    number_list = lines[0].split(',')
    boards = get_boards(lines)

    for num in number_list:
        winner = False
        for i in range(len(boards)):
            boards[i] = update_board(boards[i], num)
            if bingo(boards[i]):
                board_sum = sum_board(boards[i])
                print(f"{num=}")
                print(f"{board_sum=}")
                print(f"product = {int(num) * board_sum}")
                winner = True
                break
        if winner:
            break

    return


def part2():
    lines = get_lines(INPUT_FILE)
    number_list = lines[0].split(',')
    boards = get_boards(lines)
    winners_list = list()
    winners = list()
    for num in number_list:
        for i in range(len(boards)):
            if i not in winners_list:
                boards[i] = update_board(boards[i], num)
                if bingo(boards[i]):
                    board_sum = sum_board(boards[i])
                    winners.append((int(num), board_sum))
                    winners_list.append(i)

    print(winners)
    last_winner = winners[-1]
    print(last_winner)
    print(last_winner[0] * last_winner[1])
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
