'''
02\04\24

208. Implement Trie (Prefix Tree)string

Medium

https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/

Accepted
1M
Submissions
1.6M
Acceptance Rate
64.9%


Memory
29.15
MB
Beats
88.57%
of users with Python3   `1

Runtime
106
ms
Beats
91.02%
of users with Python3
'''

class Trie:

    def __init__(self):
        self.root = dict()
        self.items = set()


    def insert(self, word: str) -> None:
        curr_chars = [new_char for new_char in word]
        prev_char = self.root
        for curr_char in curr_chars:
            if curr_char not in prev_char:
                prev_char[curr_char] = dict()
            prev_char = prev_char[curr_char]

        self.items.add(word)



    def search(self, word: str) -> bool:
        return word in self.items



    def startsWith(self, prefix: str) -> bool:
        curr_chars = [new_char for new_char in prefix]
        prev_char = self.root
        for curr_char in curr_chars:
            if curr_char not in prev_char:
                return False
            prev_char = prev_char[curr_char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")
    trie.insert("rental")

    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))

    trie.insert("app")
    print(trie.search("app"))

