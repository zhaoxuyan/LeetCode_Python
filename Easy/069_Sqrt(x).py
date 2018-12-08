# 示例 1:
# 输入: 4
# 输出: 2

# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            return 'error'
        else:
            i = 1
            while True:
                if (i + 1) ** 2 > x >= i ** 2:
                    return i
                i += 1

    def mySqrtLeetCode(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower = 0
        upper = x

        while lower <= upper:
            middle = (lower + upper) // 2
            temp = middle * middle
            if middle * middle <= x < (middle + 1) * (middle + 1):
                return middle
            elif temp > x:
                upper = middle - 1
            else:
                lower = middle + 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.mySqrtLeetCode(8))
