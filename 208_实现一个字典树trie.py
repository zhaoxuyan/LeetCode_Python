# -*- coding: utf-8 -*- 
# @Time    : 2020/1/3 17:07
# @Author  : zhaoxuyan
# @FileName: 208_实现一个字典树trie.py
# @Software: PyCharm
class Trie:
    def __init__(self):
        # 字典 {}
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        # 注意是复制地址过来了
        node = self.root
        for char in word:
            # setdefault类似于get, 获取值
            # 如果char为node中的key，则将值取出来
            # 如果char 这个key 不存在，则设置新的key, char : {}
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
        # {'f': {'i': {'s': {'h': {'#': '#'}}}}}
        # print(self.root)

    def search(self, word: str) -> bool:
        """
        search 是要全部字符看完
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # 是要全部字符看完
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("fish")
    # print(obj.search("apple"))
