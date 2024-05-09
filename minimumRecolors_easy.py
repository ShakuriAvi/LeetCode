'''
09\05\24

2379. Minimum Recolors to Get K Consecutive Black Blocks

https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

String
Easy

Accepted
51.1K
Submissions
87.2K
Acceptance Rate
58.6%

Memory
16.56
MB
Beats
63.87%
of users with Python3

Runtime
33
ms
Beats
79.45%
of users with Python3

'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) < k:
            return 0
        min_recolor = 0
        for i in range(k):
            if blocks[i] == 'W':
                min_recolor += 1
        start, end = 0, len(blocks) - 1
        temp_min_recolor = min_recolor
        while start + k <= end:
            if blocks[start] == 'W':
                temp_min_recolor -= 1

            if blocks[start + k] == 'W':
                temp_min_recolor += 1

            min_recolor = min(temp_min_recolor, min_recolor)
            start += 1

        return min_recolor if min_recolor >= 0 else 0



if __name__ == '__main__':
    sol = Solution()
    # print(sol.minimumRecolors("WBBWWBBWBW", 7))
    # print(sol.minimumRecolors("WBWBBBW", 2))
    print(sol.minimumRecolors("WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", 15))
