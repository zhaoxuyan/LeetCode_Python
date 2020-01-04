# 示例 1:
# 输入: 4
# 输出: 2

# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
class Solution:
    # 二分查找
    # 因为y=x^2是单调递增的
    def mySqrtBinarySearch(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x

        while left <= right:
            # 返回整数部分
            # mid = (left + right) // 2
            # temp = mid * mid
            # if mid * mid <= x < (mid + 1) * (mid + 1):
            #     return mid
            # elif temp > x:
            #     right = mid - 1
            # else:
            #     left = mid + 1

            # 尽可能精确
            mid = (left + right) / 2
            temp = mid * mid
            if abs(left - right) < 1e-9:
                return right
            elif temp > x:
                right = mid
            else:
                left = mid

    def mySqrtNewton(self, x):
        """
        牛顿迭代法
        若y = x^2 = 2

        x_{n+1} = x_{n} - f(x_{n})/f'(x_{n})
                = x_{n} - x_{n}^2 - y_0 / 2 * x_{n}
                = (x_{n} + y_0 / x_{n}) / 2
        :param x:
        :return:
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


if __name__ == '__main__':
    obj = Solution()
    print(obj.mySqrtNewton(2))
