from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = "()"

        combinations = set()

        def all_combinations(parenthesis: str, n: int):
            if n == 0:
                combinations.add(parenthesis)

            for i in range(n):
                new_parenthesis = parenthesis + "()"
                all_combinations(new_parenthesis, n-1)
                new_parenthesis = "()" + parenthesis
                all_combinations(new_parenthesis, n-1)
                new_parenthesis = "(" + parenthesis + ")"
                all_combinations(new_parenthesis, n-1)



        all_combinations(parenthesis, n-1)
        return list(combinations)






if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
