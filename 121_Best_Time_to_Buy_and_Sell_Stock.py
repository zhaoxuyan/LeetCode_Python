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
            if price < buy:
                buy = price
            if price - buy > profit:
                profit = price - buy

        return profit

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
