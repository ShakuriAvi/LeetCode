'''
05\04\24


2285. Maximum Total Importance of Roads

list

Medium

https://leetcode.com/problems/maximum-total-importance-of-roads/description/

Accepted
32.1K
Submissions
52.8K
Acceptance Rate
60.9%

Runtime
1338
ms
Beats
15.32%
of users with Python3

Memory
43.00
MB
Beats
29.44%
of users with Python3
'''

from typing import List

from collections import OrderedDict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        shows_by_city = dict()
        for road in roads:
            item1, item2 = road
            self.add_city_to_city_shows(shows_by_city, item1)
            self.add_city_to_city_shows(shows_by_city, item2)

        shows_by_city = {k: v for k, v in sorted(shows_by_city.items(), key=lambda item: -item[1])}
        for k in shows_by_city.keys():
            shows_by_city[k] = n
            n -= 1
        res = 0
        for road in roads:
            item1, item2 = road
            res += shows_by_city[item1] + shows_by_city[item2]

        return res



    def add_city_to_city_shows(self, city_shows: dict, city: int):
        if not city in city_shows:
            city_shows[city] = 0
        city_shows[city] += 1


if __name__ == '__main__':
    print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
