'''
05\04\24

Second attempt

53. Maximum Subarray
list

Medium

https://leetcode.com/problems/maximum-subarray/description/
Accepted
3.8M
Submissions
7.5M
Acceptance Rate
50.7%

Runtime
501
ms
Beats
86.34%
of users with Python3
Memory
31.21
MB
Beats
5.18%
of users with Python3
'''



from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10000000-1
        largest_sub_sum = 0
        for num in nums:
            largest_sub_sum += num
            if largest_sub_sum > max_sum:
                max_sum = largest_sub_sum
            if largest_sub_sum < 0:
                largest_sub_sum = 0
        return max_sum



if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1]))
    print(Solution().maxSubArray([5,4,-1,7,8]))
