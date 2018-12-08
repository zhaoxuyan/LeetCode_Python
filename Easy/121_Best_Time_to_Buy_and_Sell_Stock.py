# 买卖股票的最佳时机

# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意：利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。


# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 示例 3：
# 输入: [1,2,4,2,5,7,2,4,9,0,9]
# 输出: 9
class Solution:

    # 解法1：
    # 动态的找最低点买入（从左往右找），符合示例3
    def maxProfitLeetCode(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0

        profit = 0
        buy = prices[0]
        for i, price in enumerate(prices):
            # 动态的找最低点买入（从左往右找），符合示例3
            if price < buy:
                buy = price
            if price - buy > profit:
                profit = price - buy

        return profit

    # 解法2：
    # 该题解法和最大连续子数组和的解法思路是一样的。
    # 1. 根据股票的利益意义，想要更多利益则值低时买进，值高时卖出。
    #    根据提供的股票价格不方便得出股票价格变化，对原数据进行计算：list[i] - list[i - 1] = 股票的变化。
    #    变化为正时股票增长（存在利益），变化为负时股票为下跌（无利益）。
    # 2. 得到股票的变化值列表，即求最大子数组和，最后得到正解。

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_new = []
        for i in range(len(prices) - 1):
            prices_new.append(prices[i + 1] - prices[i])
        print(prices_new)

        res = self.maxSubArray(prices_new)
        if res <= 0:
            return 0
        else:
            return res

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sum = 0
        ans = nums[0]
        for number in nums:
            if sum > 0:
                sum += number
            else:
                sum = number
            if sum > ans:
                ans = sum
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfitLeetCode([7, 6, 8, 1]))
