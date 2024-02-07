#!/usr/bin/python3
"""
N Queens Problem
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed in board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, col, N, result):
    """
    Solve N queens problem using backtracking
    """
    # If all queens are placed, append solution to result
    if col >= N:
        sol = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    sol.append([i, j])
        result.append(sol)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1, N, result) or res
            board[i][col] = 0  # Backtrack

    return res


def print_board(board):
    """
    Print the board configuration
    """
    for row in board:
        print(row)


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    if not solve_n_queens(board, 0, N, result):
        print("No solution found")

    for sol in result:
        print(sol)


if __name__ == "__main__":
    main()
