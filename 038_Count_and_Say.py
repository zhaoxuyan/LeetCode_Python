# 报数
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 6==>   312211
# 7==>   13112221
import itertools


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        b = '1'  # 将第一行的1换成字符类型，便于下一行的读出
        for i in range(n - 1):  # (n-1)是因为第一行不需要处理，直接可以读出
            a = b[0]  # a用来读取上一行的第一个字符
            c = ''  # c用来存放读出的内容(char)
            count = 0  # count用来统计
            for j in b:
                if j == a:
                    count += 1
                else:
                    c += str(count) + a  # 注意一定要将count转换为字符型，否则两个数就会相加（变成数学相加）。
                    a = j
                    count = 1
            c += str(count) + a
            b = c
        return b

    def countAndSayPyton(self, n):
        # 法二：python中的itertools.groupby()可以帮助我们数连着的数字
        res = '1'
        for i in range(0, n - 1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res
