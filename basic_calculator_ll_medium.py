'''
31\03\24

227. Basic Calculator II
string

Medium

https://leetcode.com/problems/basic-calculator-ii/description/

Accepted
614.6K
Submissions
1.4M
Acceptance Rate
43.5%

Beats
46.76%
of users with Python3
Beats
59.55%
of users with Python3
'''


class Solution:
    def calculate(self, s: str) -> int:
        queue = []
        new_number = 0
        operators = ['+', '-', '*', '/', ';']
        s += ';'
        for char in s:
            if char.isdigit():
                new_number = new_number * 10 + int(char)
            elif char in operators:
                if len(queue) > 0:
                    last_operator = queue.pop()
                    if last_operator == '-':
                        new_number = -1*new_number
                    elif last_operator == '*':
                        old_number = queue.pop()
                        new_number = new_number*old_number
                    elif last_operator == '/':
                        old_number = queue.pop()
                        new_number = int(old_number/new_number)
                queue.append(new_number)
                queue.append(char)

                new_number = 0


        return sum(num for num in queue if type(num)==int)





if __name__ == '__main__':
    print(Solution().calculate("3+2*2"))
    print(Solution().calculate(" 3/2 "))
    print(Solution().calculate(" 3+5 / 2 "))
    print(Solution().calculate("2*3*4"))
