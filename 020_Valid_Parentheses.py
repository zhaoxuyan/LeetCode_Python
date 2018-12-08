# 示例 1:
# 输入: "()"
# 输出: true

# 示例 2:
# 输入: "()[]{}"
# 输出: true

# 示例 3:
# 输入: "(]"
# 输出: false

# 示例 4:
# 输入: "([)]"
# 输出: false

# 示例 5:
# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 奇数永远无法配对
        # 当然还有len(s) == 0
        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True

        d = {'{': '}', '[': ']', '(': ')'}
        # 用栈来解决
        stack = []
        for i in s:
            # in stack
            if i in d:
                stack.append(i)
            else:
                if stack == [] or d[stack.pop()] != i:  # 如果栈为空或者栈顶的元素不是i的范括号
                    return False

        return stack == []
