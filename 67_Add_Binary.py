# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"

# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 二进制到十进制
        res = int(a, 2) + int(b, 2)
        # 十进制到二进制
        return bin(res)[2:]
