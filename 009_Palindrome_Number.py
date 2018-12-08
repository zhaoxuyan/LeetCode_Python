# 判断是否是回文数
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = len(str(x))
        if x < 0:
            return False
        if n == 1:
            return True
        # 如果x是偶数
        if x % 2 == 0:
            mid = n // 2 - 1
            return str(x)[0:mid + 1] == str(x)[mid + 1:][::-1]
        else:
            mid = n // 2
            return str(x)[0:mid] == str(x)[mid+1:][::-1]

    def isPalindromeEasy(self, x):
        if x >= 0 and str(x) == str(x)[::-1]:
            a = True
        else:
            a = False
        return a
