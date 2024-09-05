from typing import List
from collections import deque
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        place_by_start = dict()
        intervals = deque(intervals)
        copy_deque = intervals.copy()
        idx = 0
        max_start = -1
        while copy_deque:
            start, end = copy_deque.popleft()
            place_by_start[start] = idx
            max_start = max(max_start, start)
            idx += 1

        res = []
        while intervals:
            start, end = intervals.popleft()
            if end in place_by_start:
                res.append(place_by_start[end])
            elif end < max_start:
                for i in range(end,max_start+1):
                    if i in place_by_start:
                        res.append(place_by_start[i])
                        break
            else:
                res.append(-1)

        return res

if __name__ == '__main__':
    sol = Solution()
    # print(sol.findRightInterval([[3,4],[2,3],[1,2]]))
    # print(sol.findRightInterval([[4,5],[2,3],[1,2]]))
    print(sol.findRightInterval([[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]))




