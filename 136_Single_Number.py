# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
# 输入: [2,2,1]
# 输出: 1

# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4


# 4.      找出非成对的数
# 一大串数,成双成对,只有一个落单.如果快速揪出来?
# 根据性质1,异或所有数,所有成双成对的都挂掉了.我们就可以在一大串数中找到落单的.
# A^B^C^D^C^B^A=D.被揪出来了.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.singleNumber([4, 1, 2, 1, 2]))
