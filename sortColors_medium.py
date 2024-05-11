'''
11\05\24

75. Sort Colors
https://leetcode.com/problems/sort-colors/description/

Accepted
1.9M
Submissions
3.1M
Acceptance Rate
62.3%

Memory
16.48
MB
Beats
89.76%
of users with Python3

Runtime
39
ms
Beats
46.60%
of users with Python3
'''

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst_buckets = [0] * 3
        for color in nums:
            lst_buckets[color] += 1
        counter = 0
        for idx in range(len(lst_buckets)):
            end = counter + lst_buckets[idx]
            while counter < end:
                nums[counter] = idx
                counter += 1

if __name__ == '__main__':
    print(Solution().sortColors([2, 0, 2, 1, 1, 0]))