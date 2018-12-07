# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_number = ''
        for number in digits:
            str_number += str(number)
        res_number = int(str_number) + 1

        res = []
        while res_number > 0:
            res.append(res_number % 10)
            res_number //= 10
        return res[::-1]
