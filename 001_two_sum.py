# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j
                else:
                    continue

    def twoSumMap(self, nums, target):
        n = len(nums)
        map = {}
        for i in range(n):
            map[nums[i]] = i
        for i in range(n):
            component = target - nums[i]
            if map.__contains__(component) and map.get(component) != i:
                return i, map.get(component)
