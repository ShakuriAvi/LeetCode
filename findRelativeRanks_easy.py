from queue import PriorityQueue

from typing import List
class Score:
    def __init__(self, item: int):
        self.item = item

    def __lt__(self, other):

        return self.item > other.item
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        idx = 0
        res = []

        queue = PriorityQueue()
        for item in score:
            queue.put((-1 * item, idx))
            idx += 1
        while not queue.empty():
            item, idx = queue.get()
            if idx > 2:
                res.append(idx+1)
            else:
                res.append(rank[idx])


        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findRelativeRanks([5,4,3,2,1]))
    print(sol.findRelativeRanks([10,3,8,9,4]))
