'''
04\05\24

2210. Count Hills and Valleys in an Array

https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

Binary Tree
medium

Accepted
45.7K
Submissions
76.1K
Acceptance Rate
60.1%

Memory
Beats
16.41%
of users with Python3

Runtime
Beats
93.88%
of users with Python3
'''
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills_and_valleys_counter = 0
        idx = -1
        updated_nums = []
        last_idx = len(nums) - 1
        while idx < last_idx:
            idx += 1
            if idx != len(nums) -1 and nums[idx] == nums[idx+1]:
                continue
            updated_nums.append(nums[idx])

        idx = 1
        last_idx = len(updated_nums) - 1
        while idx < last_idx:
            if ((updated_nums[idx] < updated_nums[idx+1] and updated_nums[idx] < updated_nums[idx-1]) or
                    updated_nums[idx] > updated_nums[idx+1] and updated_nums[idx] > updated_nums[idx-1]):
                hills_and_valleys_counter += 1
            idx += 1


        return hills_and_valleys_counter

if __name__ == '__main__':
    print(Solution().countHillValley([2, 4, 1, 1, 6, 5]))
    print(Solution().countHillValley([6, 6, 5, 5, 4, 1]))
