# -*- coding: utf-8 -*- 
# @Time    : 2020/1/3 13:09
# @Author  : zhaoxuyan
# @FileName: 036_有效的数独.py
# @Software: PyCharm

# 使用line,column,和子区域来分别保存元素,如果元素有重复的就返回false,否则返回true即可. 在这里巧用了一下集合.
# 判断某个元素是否在集合中时间复杂度是O(1),如果使用列表的话就是O(n)了.
# 其中划分子区域的技巧很巧妙,使用的是 pos = (i//3)*3 + j//3.
class Solution:
    def isValidSudoku(self, board) -> bool:
        matrix_line = [set() for i in range(9)]
        matrix_column = [set() for i in range(9)]
        matrix_area = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                pos = (i // 3) * 3 + j // 3
                if item != '.':
                    if item not in matrix_line[i] and item not in matrix_column[j] and item not in matrix_area[pos]:
                        matrix_line[i].add(item)
                        matrix_column[j].add(item)
                        matrix_area[pos].add(item)
                    else:
                        return False
        return True
