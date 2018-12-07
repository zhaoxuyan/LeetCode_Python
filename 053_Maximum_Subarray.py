# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 输入: [-1,-2]
# 输出: [-1]

# 思路：
# 如果sum已经被抵消到小于0了，例如数组[1,2,3,-3,-2,-2,3,4]，
# 累加到第6个数时，sum已经小于(或等于)0了，这6个数的和对于后面元素的累加已经没有益处了（不能使得序列的和变大了），
# 则令sum=number，开始一个新的子序列的累加过程。


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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

    def maxSubArrayBaoli(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            sub = max(nums[i] + nums[i - 1], nums[i])
            nums[i] = sub  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
        return max(nums)


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([-1, -2]))
