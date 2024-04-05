'''
03\04\24

20. Valid Parentheses
Medium

https://leetcode.com/problems/valid-parentheses/description
4.4M
Submissions
11M
Acceptance Rate
40.5%


Memory
16.60
MB
Beats
75.34%
of users with Python3

Runtime
24
ms
Beats
98.09%
of users with Python3
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        open_bracket = {"[":"]","{":"}","(":")"}
        for parentheses in s:
            if parentheses in open_bracket:
                stack.append(parentheses)
                continue

            if len(stack) == 0 or open_bracket[stack[-1]] != parentheses:
                return False
            stack.pop()


        return len(stack) == 0




        pass

if __name__ == '__main__':
    # print(Solution().isValid("()"))
    # print(Solution().isValid("()[]{}"))
    # print(Solution().isValid("(]"))
    print(Solution().isValid("]"))

