'''
29\06\24
second attempt
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/description/

Accepted
419.1K
Submissions
584.1K
Acceptance Rate
71.7%

Memory
17.44
MB
Beats
69.81%


Runtime
132
ms
Beats
12.83%

'''
from typing import List
import collections

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        union_items = firstList + secondList
        union_items.sort(key = lambda x: (x[0] , x[1]))
        union_items = collections.deque(union_items)
        res = []
        first_start, first_end = union_items.popleft()
        while union_items:
            second_start, second_end = union_items.popleft()
            if first_end == second_start:
                res.append([first_end, second_start])
            elif first_end > second_start:
                if first_end <= second_end:
                    res.append([second_start, first_end])
                else:
                    res.append([second_start, second_end])

            if first_end > second_end:
                continue
            first_start, first_end = second_start, second_end

        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.intervalIntersection([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]]))

    # print(sol.intervalIntersection( [[5,10]], [[5,6]]))
    # print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
