'''
30\06\24
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

Accepted
827.8K
Submissions
1.2M
Acceptance Rate
68.3%

Memory
30.56
MB
Beats
84.55%


Runtime
452
ms
Beats
59.62%

'''

from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        middle = int((end - start) // 2)

        max_item = -1
        max_idx = -1
        while start + 1 < end:
            if arr[middle] > arr[middle + 1]:
                end = middle
            else:
                start = middle

            if max_item < arr[middle]:
                max_item = arr[middle]
                max_idx = middle
            middle = start + ((end - start) // 2)

        return max_idx


        return max_item
if __name__ == '__main__':
    sol = Solution()
    sol.peakIndexInMountainArray([3,4,5,1])