'''
02\04\24

1003. Check If Word Is Valid After Substitutions
string

Medium

https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/

Accepted
60.5K
Submissions
101.9K
Acceptance Rate
59.4%


Memory
16.55
MB
Beats
96.87%
of users with Python3

Runtime
34
ms
Beats
93.99%
of users with Python3
'''


class Solution:
    def isValid(self, s: str) -> bool:
        return self.check_string(s)

    def check_string(self,s):
        if len(s) == 0:
            return True

        if "abc" not in s:
            return False

        return self.check_string(s.replace("abc", ""))



if __name__ == '__main__':
    print(Solution().isValid("aabcbc"))
    print(Solution().isValid("abcabcababcc"))
    print(Solution().isValid("abccba"))

