'''
11\05\24

17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Accepted
2M
Submissions
3.3M
Acceptance Rate
60.5%

Memory
16.55
MB
Beats
41.27%
of users with Python3

Runtime
42
ms
Beats
12.09%
of users with Python3
'''


from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["-1", "-1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        input_letters = []
        if len(digits) == 0:
            return []
        for i in range(len(digits)):
            input_letters.append(letters[int(digits[i])])

        combinations = set()
        def all_combinations(input_letters: List[str], idx: int, item:str):
            if len(item) == len(input_letters):
                combinations.add(item)
                return
            for letter_idx in range(len(input_letters[idx])):
                letter = item + input_letters[idx][letter_idx]
                all_combinations(input_letters, idx+1, letter)

        all_combinations(input_letters, 0, "")
        return list(combinations)




if __name__ == '__main__':
    print(Solution().letterCombinations("23"))