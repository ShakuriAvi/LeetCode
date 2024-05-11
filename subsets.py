'''
11\05\24

78. Subsets
https://leetcode.com/problems/subsets/description/
Accepted
1.8M
Submissions
2.4M
Acceptance Rate
77.5%

Memory
16.59
MB
Beats
98.02%
of users with Python3

Runtime
39
ms
Beats
44.86%
of users with Python3
'''


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subset = []
        def all_possible_subset(nums_list: List[int] , idx):
            nonlocal all_subset
            if idx == len(nums):
                all_subset.append(nums_list)
                return

            all_subset.append(nums_list)
            for i in range(idx, len(nums)):
                new_list = nums_list.copy()
                new_list.append(nums[i])
                all_possible_subset(new_list, i+1)

        all_possible_subset([], 0)
        return all_subset



if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))