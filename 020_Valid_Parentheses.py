# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串
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

        template = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            # 如果是正括号
            if i in template:
                stack.append(i)
            # 如果是反括号
            elif stack == [] or template[stack.pop()] != i:
                return False
        return stack == []


if __name__ == '__main__':
    obj = Solution()
    print(obj.isValid("[()"))
