# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        ans = strs[0]
        for str in strs:
            ans = self.findLongestCommonWord(str, ans)
        return ans

    # 两两比较
    def findLongestCommonWord(self, str1, str2):

        # 首先判断：短的放前面，长的放后面
        # 如果不满足则交换
        if len(str1) > len(str2):
            return self.findLongestCommonWord(str2, str1)

        if len(str1) == 0:
            return ''

        ans = ''
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                ans += str1[i]
            else:
                break
        return ans
