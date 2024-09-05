'''
27\06\24

2442. Count Number of Distinct Integers After Reverse Operations
https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/

Accepted
62.4K
Submissions
78.5K
Acceptance Rate
79.5%

Memory
42.16
MB
Beats
61.12%

Runtime
497
ms
Beats
89.83%

'''
from typing import List
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)
        for num in nums:
            num_str = str(num)
            num_str = num_str[::-1]
            res.add(int(num_str))
        return len(res)


if __name__ == '__main__':
    sol = Solution()
    sol.countDistinctIntegers([1,13,10,12,31])


