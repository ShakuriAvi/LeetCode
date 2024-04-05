'''

05\04\24

2126. Destroying Asteroids
list

Medium

https://leetcode.com/problems/destroying-asteroids/description/

Accepted
41.6K
Submissions
80.9K
Acceptance Rate
51.4%

Memory
30.35
MB
Beats
65.94%
of users with Python3

Runtime
848
ms
Beats
26.22%
of users with Python3
'''

from typing import List
class Solution:

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        idx = 0
        while idx < len(asteroids):
            if asteroids[idx] > mass:
                return False
            mass += asteroids[idx]
            idx += 1
        return True


if __name__ == '__main__':
    print(Solution().asteroidsDestroyed(10,[3,9,19,5,21]))
    print(Solution().asteroidsDestroyed(5,[4,9,23,4]))
