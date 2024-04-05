'''
05\04\24


15. 3Sum

list

Medium

https://leetcode.com/problems/3sum/description/

Accepted
3.4M
Submissions
10M
Acceptance Rate
34.4%

Runtime
1709
ms
Beats
14.64%
of users with Python3

Memory
21.93
MB
Beats
6.71%
of users with Python3
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        prev = -float('inf')
        for i in range(len(nums)-2):
            if prev == nums[i]: continue

            res_by_vals = dict()
            for j in range(i + 1, len(nums)):
                negative_val = (-1) * nums[j]
                if negative_val not in res_by_vals:
                    res_by_vals[nums[j] + nums[i]] = [nums[j], nums[i]]
                else:
                    res.add((res_by_vals[negative_val][0], res_by_vals[negative_val][1], nums[j]))

            prev = nums[i]

        return [list(re) for re in res]

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))