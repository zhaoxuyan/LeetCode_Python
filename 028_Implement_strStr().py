# 给定一个 haystack 字符串和一个 needle 字符串:
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2

# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 用字符串的内建函数s.find()
        return haystack.find(needle)

    def strStrEasySplit(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):  # 有效减少比较的次数
            if haystack[i:i + len(needle)] == needle:  # 字符串切片操作可以直接比较一个子串，不用每个字符都比较
                return i
        return -1
