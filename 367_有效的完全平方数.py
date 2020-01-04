# -*- coding: utf-8 -*- 
# @Time    : 2020/1/3 16:29
# @Author  : zhaoxuyan
# @FileName: 367_有效的完全平方数.py
# @Software: PyCharm
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            # 返回整数部分
            mid = (left + right) // 2
            temp = mid * mid
            if mid * mid == num:
                return mid
            elif temp > num:
                right = mid - 1
            else:
                left = mid + 1
