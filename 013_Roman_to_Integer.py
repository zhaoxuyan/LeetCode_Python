#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    dic = {}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 必须加一个这样的if判断 否则会超时
        if self.dic.__len__() == 0:
            for i in range(4000):
                j = i
                one = j % 10
                j //= 10
                ten = j % 10
                j //= 10
                h = j % 10
                j //= 10
                t = j
                ans = 'M' * t + 'C' * h + 'X' * ten + 'I' * one

                # 9 5 4
                if ans.__contains__('I' * 9):
                    ans = ans.replace('I' * 9, 'IX')
                if ans.__contains__('I' * 5):
                    ans = ans.replace('I' * 5, 'V')
                if ans.__contains__('I' * 4):
                    ans = ans.replace('I' * 4, 'IV')

                # 90 50 40
                if ans.__contains__('X' * 9):
                    ans = ans.replace('X' * 9, 'XC')
                if ans.__contains__('X' * 5):
                    ans = ans.replace('X' * 5, 'L')
                if ans.__contains__('X' * 4):
                    ans = ans.replace('X' * 4, 'XL')

                # 900 500 400
                if ans.__contains__('C' * 9):
                    ans = ans.replace('C' * 9, 'CM')
                if ans.__contains__('C' * 5):
                    ans = ans.replace('C' * 5, 'D')
                if ans.__contains__('C' * 4):
                    ans = ans.replace('C' * 4, 'CD')
                self.dic[ans] = i

        return self.dic.get(s)


if __name__ == '__main__':
    obj = Solution()
    print(obj.romanToInt("III"))
