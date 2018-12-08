# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。

# 输入: "Hello World"
# 输出: 5
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == ' ':
            return 0
        elif len(s) == 1 and s != ' ':
            return 1
        else:
            split_res = s.rstrip().split(' ')
            return len(split_res[::-1][0])

