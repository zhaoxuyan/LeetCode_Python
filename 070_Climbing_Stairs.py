# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
#
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# n<=1，此时只有一种。
# n>1时，对于每一个台阶i，要到达台阶，最后一步都有两种方法，从i-1迈一步，或从i-2迈两步。
# 本质上是一个Fibonacci数列

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        ans = []
        ans.append(1)
        ans.append(2)
        ans.append(3)
        for i in range(3, n):
            ans.append(ans[-1] + ans[-2])
        return ans[-1]
