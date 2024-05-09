'''
06\04\24
List
Medium

435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/submissions/1224636715/

Accepted
547.5K
Submissions
1M
Acceptance Rate
53.1%

Runtime
1040
ms
Beats
77.79%
of users with Python3

Memory
55.22
MB
Beats
57.16%
of users with Python3
'''

from typing import List
from collections import OrderedDict
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        k = float('-inf')
        intervals.sort(key = lambda x : x[1])
        for i in range(len(intervals)):
            if intervals[i][0] >= k:
                k = intervals[i][1]
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    # print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    # print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    # print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))
    # print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    # print(Solution().eraseOverlapIntervals([[0,1],[3,4],[1,2]]))
    print(Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))


'''
        start_end_intervals = dict()
        for start, end in intervals:
            if start not in start_end_intervals:
                start_end_intervals[start] = end
            else:
                start_end_intervals[start] = min(start_end_intervals[start], end)

        next_end =float('-inf')
        start_end_intervals = OrderedDict(sorted(start_end_intervals.items()))
        items_count = 0
        for start, end in start_end_intervals.items():
            if start >= next_end:
                items_count += 1
                next_end = end


        return len(intervals) - items_count

'''

