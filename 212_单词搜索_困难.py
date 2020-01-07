# -*- coding: utf-8 -*- 
# @Time    : 2020/1/6 16:49
# @Author  : zhaoxuyan
# @FileName: 212_单词搜索_困难.py
# @Software: PyCharm

# https://leetcode-cn.com/problems/word-search-ii/comments/

# 第一种方法 纯DFS
# 第二种方法 DFS + 字典树Trie
# 因为候选词是确定的, 先将候选测放入Trie中

# 方向数组
# 四连通图 上下左右
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

END_OF_WORD = "#"


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.result = set()

    def findWords(self, board, words):
        if not board or not board[0]:
            return []
        if not words:
            return []

        # 构造字典树
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        # 开始dfs遍历
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)
        return self.result

    def dfs(self, board, i, j, cur_word, cur_dict):
        # 单词拼装
        cur_word += board[i][j]
        # 一层一层往下
        cur_dict = cur_dict[board[i][j]]

        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        # 将board[i][j]保存起来
        temp = board[i][j]
        # board[i][j]访问过, 当前不能再用了, 用@作为标记
        board[i][j] = "@"

        # 尝试四个方向
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n \
                    and board[x][y] != "@" \
                    and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        # 回溯
        board[i][j] = temp
