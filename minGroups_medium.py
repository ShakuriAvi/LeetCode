from typing import List
from heapq import heappop, heappush
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]), reverse=True)
        res = [intervals.pop()[1]]
        while intervals:
            start_item, end_item = intervals.pop()
            if start_item > res[0]:
                heappop(res)
            heappush(res, end_item)

        return len(res)




        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
    print(sol.minGroups([[1,3],[5,6],[8,10],[11,13]]))
