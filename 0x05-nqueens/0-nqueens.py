#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. Write a
program that solves the N queens problem."""

from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    content = []

    def solve_queens(val, n, content):
        if (val == n):
            print(content)
        else:
            for col in range(n):
                res = [val, col]
                if valid_res(content, res):
                    content.append(res)
                    solve_queens(val + 1, n, content)
                    content.remove(res)

    def valid_res(content, res):
        for que in content:
            if que[1] == res[1]:
                return False
            if (que[0] + que[1]) == (res[0] + res[1]):
                return False
            if (que[0] - que[1]) == (res[0] - res[1]):
                return False
        return True


solve_queens(0, n, content)
