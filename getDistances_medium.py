from typing import List
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        item_by_pos = dict()
        res = [0] * len(arr)
        for i in range(0, len(arr)):
            item = arr[i]
            if item not in item_by_pos:
                item_by_pos[item] = set()
            item_by_pos[item].add(i)


        for i in range(0, len(arr)):
            item = arr[i]
            sum_idx = abs((i*len(item_by_pos[item])) - sum(item_by_pos[item]))

            for val in item_by_pos[item]:
                sum_idx += abs(i-val)
            res.append(sum_idx)
        return res





if __name__ == '__main__':
    sol = Solution()
    sol.getDistances([2,1,3,1,2,3,3])