class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        char_by_value = {"b":0, "a":0}
        equal_str = 0
        if len(a) == len(b):
            word_length = len(a)

            for i in range(word_length):
                if ord(b[i]) > ord(a[i]):
                    char_by_value["b"] +=1
                elif ord(b[i]) < ord(a[i]):
                    char_by_value["a"] +=1
                else:
                    equal_str +=1

            max_val = max([item for item in char_by_value.values()])

            return word_length - max_val if max_val >= equal_str else word_length - equal_str  + 1
        else:
            max_word = max([ord(word) for word in a],[ord(word) for word in a])
            if max_word in b and len(b) < len(a):
                return len(b.replace(max_word,''))
            return len(a.replace(max_word,''))



if __name__ == '__main__':
    # print(Solution().minCharacters("aba","caa"))
    print(Solution().minCharacters("dabadd","cda"))

