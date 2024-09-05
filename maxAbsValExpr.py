from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max_res = 0
        for i in range(len(arr1)-1):
            for j in range(i+1, len(arr1)):
                max_res = max(max_res, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i-j))

        return max_res
if __name__ == '__main__':
    print(Solution().maxAbsValExpr([1,2,3,4], [-1,4,5,6]))
    print(Solution().maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]))


