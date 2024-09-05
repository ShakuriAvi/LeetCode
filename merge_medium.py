'''
29\06\24
second attempt
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

Accepted
2.5M
Submissions
5.2M
Acceptance Rate
47.6%

Memory
21.62
MB
Beats
6.24%

Runtime
126
ms
Beats
41.79%

'''

from typing import List
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        intervals = deque(intervals)
        min_start, max_end = intervals.popleft()
        res = []
        while intervals:
            item_start, item_end = intervals.popleft()

            if max_end < item_start:
                res.append([min_start, max_end])
                min_start, max_end = item_start, item_end
            else:
                max_end = max(item_end, max_end)


        res.append([min_start, max_end])
        return res






if __name__ == '__main__':
    sol = Solution()
    # sol.merge([[1,3],[2,6],[8,10],[15,18]])

    # print(sol.merge([[1,4],[4,5]]))
    # print(sol.merge([[1,4],[5,6]]))
    sol.merge([[1,4],[2,3]])

