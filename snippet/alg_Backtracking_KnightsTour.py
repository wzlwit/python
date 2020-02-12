"""
递归回溯法：又称为试探法(heuristic)，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""

import sys
import time

# SIZE = 3      # 0 ways
# SIZE = 4      # 0 ways
SIZE = 5      # 304 ways
# SIZE = 6      # ? ways
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    # if row >= 0 and row < SIZE and \
    #         col >= 0 and col < SIZE and \
    #         board[row][col] == 0:
    #     board[row][col] = step
    if 0 <= row < SIZE and 0 <= col < SIZE and board[row][col] == 0:
        board[row][col] = step

        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)

        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, 0, 0)
    # patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()