# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。

# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if i >= 1:
                if nums[i - 1] < target < nums[i]:
                    return i
            else:
                if target < nums[i]:
                    return 0
            if target > nums[len(nums) - 1]:
                return len(nums)

    def searchInsertPython(self, nums, target):
        # 如果有重复元素
        if nums.count(target) > 0:
            return nums.find(target)
        else:
            # 找到第一个比target大的元素即可
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)
