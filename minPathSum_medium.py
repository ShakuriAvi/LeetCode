'''
second attempt
28\06\24

64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/description/

Accepted
1.2M
Submissions
1.9M
Acceptance Rate
64.3%

Memory
18.32
MB
Beats
40.56%

Runtime
85
ms
Beats
54.52%

'''

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for idx in range(1, row):
            grid[idx][0] += grid[idx-1][0]

        for idx in range(1, col):
            grid[0][idx] += grid[0][idx-1]

        for i in range(1,row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[row-1][col-1]


    def bfs(self,  grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = [(0, 0, 0)]
        items = []
        while queue:
            row, col, res = queue.pop(0)
            res = res+grid[row][col]
            if row+1 == ROWS and col+1 == COLS:
                items.append(res)
                continue

            if row+1 < ROWS:
                queue.append((row + 1, col, res))

            if col+1 < COLS:
                queue.append((row, col + 1, res))

        return min(items)



if __name__ == '__main__':
    sol = Solution()
    # sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    sol.minPathSum([[1,2],[1,1]])

