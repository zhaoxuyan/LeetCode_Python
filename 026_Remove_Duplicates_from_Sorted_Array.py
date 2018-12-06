# 删除排序数组中的重复项
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 1
        # while i < len(nums):
        #     if nums[i] == nums[i - 1]:
        #         del nums[i]
        #     else:
        #         i += 1
        # return len(nums)
        
        for i in range(1, len(nums)):
            if i < len(nums):  # 用 for 循环，必须要加一个判断，否则会数组越界
                if nums[i] == nums[i - 1]:
                    del nums[i]
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 5]
    obj = Solution()
    print(obj.removeDuplicates(nums))
