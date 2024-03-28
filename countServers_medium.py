'''
28\03\24

1267. Count Servers that Communicate

array 2D

Medium

https://leetcode.com/problems/count-servers-that-communicate/description/

"Accepted
57.9K
Submissions
96.2K
Acceptance Rate
60.2%"


"Memory
18.39
MB
Beats
37.20%
of users with Python3.   Runtime
380
ms
Beats
40.58%
of users with Python3"


'''

from typing import List,Set
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        communicate_server = set()
        for i in range(m):
            self.__count_communicate_rows(grid, i, communicate_server)
        for i in range(n):
            self.__count_communicate_cols(grid, i, m, communicate_server)

        return len(communicate_server)

    def __count_communicate_rows(self, matrix: List[List[int]], row, communicate_server: Set):
        communicate_by_row = {(row, col) for col, val in enumerate(matrix[row]) if val == 1}
        if len(communicate_by_row) > 1:
            communicate_server |= communicate_by_row



    def __count_communicate_cols(self, matrix: List[List[int]], col, rows, communicate_server: Set):
        communicate_by_col = {(row, col) for row in range(rows) if matrix[row][col] == 1}
        if len(communicate_by_col) > 1:
            communicate_server |= communicate_by_col

'''
"class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = list(map(sum, grid))
        cols = list(map(sum, zip(*grid)))
        
        res = 0
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                res += 1

        return res"

'''