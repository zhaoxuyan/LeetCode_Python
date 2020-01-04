# -*- coding: utf-8 -*- 
# @Time    : 2020/1/3 13:19
# @Author  : zhaoxuyan
# @FileName: 037_解数独.py
# @Software: PyCharm

# https://leetcode-cn.com/problems/sudoku-solver/
def isValid(board, row, col, c) -> bool:
    for i in range(9):
        # 检查行中是否有c
        if board[row][i] != '.' and board[row][i] == c:
            return False
        # 检查列中是否有c
        if board[i][col] != '.' and board[i][col] == c:
            return False
        # 检查3x3的框中是否有c
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
                            3 * (col // 3) + i % 3] == c:
            return False
    return True


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or not len(board):
            return
        self.solve(board)

    def solve(self, board) -> bool:
        for i in range(len(board)):  # 行
            for j in range(len(board[0])):  # 列
                # 找空白处
                if board[i][j] == '.':
                    for c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        # isValid: 在 board的i j 位置填c
                        if isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                # 回溯, 还原
                                board[i][j] = '.'
                    return False
        return True
