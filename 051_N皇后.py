# -*- coding: utf-8 -*- 
# @Time    : 2020/1/2 20:52
# @Author  : zhaoxuyan
# @FileName: 051_N皇后.py
# @Software: PyCharm

# https://leetcode-cn.com/problems/n-queens/
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
class Solution:
    def __init__(self):
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

    def solveNQueens(self, n):
        if n < 1:
            return []
        self.DFS(n, 0, [])
        return self.generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            # 列(j) 撇(i+j) 捺(i-j)
            if col in self.cols or row + col in self.pie or row - col in self.na:
                # 这个位置不能放皇后
                continue
            else:
                self.cols.add(col)
                self.pie.add(row + col)
                self.na.add(row - col)

                # cur_state 存放满足条件的皇后位置
                self.DFS(n, row + 1, cur_state + [col])

                # 回溯
                # 如果接下来的尝试中 每个位置(列)都不可以 return了
                # 注意python set中的remove和discard的区别
                # remove 如果没有,会报错/ discard不会报错
                self.cols.remove(col)
                self.pie.remove(row + col)
                self.na.remove(row - col)

    def generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        for i in range(0, len(board), n):
            return [board[i: i + n]]
