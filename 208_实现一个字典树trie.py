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
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # setdefault类似于get
            # 如果char为node中的key，则将值取出来
            # 如果char 这个key 不存在，则设置新的key, char : {}
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
