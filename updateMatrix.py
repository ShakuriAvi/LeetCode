'''
07\04\2024

542. 01 Matrix

DP
Medium

https://leetcode.com/problems/01-matrix/description/

Accepted
544.1K
Submissions
1.1M
Acceptance Rate
48.3%

'''

from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_row = len(mat)
        max_col = len(mat[0])
        res = [[float('inf') for _ in range(max_col)] for _ in range(max_row)]
        queue = []
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(max_row):
            for j in range(max_col):
                 if mat[i][j] == 0:
                    queue.append((i,j))
                    res[i][j] = 0


        while queue:
            row, col = queue.pop(0)
            for dx, dy in direction:
                dx = dx + row
                dy = dy + col

                if 0<=dx<max_row and 0<=dy<max_col and res[dx][dy] > mat[row][col] + 1:
                    res[dx][dy] = res[row][col] +1
                    queue.append((dx, dy))

        return res







if __name__ == '__main__':
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

