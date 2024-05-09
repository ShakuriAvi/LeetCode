from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        midd = ((len(nums)) // 2)

        if nums[midd] > nums[-1]:
            if nums[-1] > target:
                pass
            elif nums[0] < target:
                return self.binary_search(nums, target, 0, midd)
        else:
            return self.binary_search(nums, target,0, len(nums) - 1)


        pass
    def binary_search(self, nums: List[int], target: int, start, end) -> int:
        midd = ((end-start) // 2) + start
        if start >= end:
            return midd if nums[start] == target else -1

        if nums[midd] < target:
            start = midd if midd != start else end
            return self.binary_search(nums,target,start,end)
        else:
            end = midd
            return self.binary_search(nums,target, start, end)


if __name__ == '__main__':
    # print(Solution().numRabbits([1,1,2]))
    # print(Solution().numRabbits([10,10,10]))
    # print(Solution().search([4,5,6,7,0,1,2],0))
    # print(Solution().search([4,5,6,7,0,1,2],3))
    print(Solution().search([3,1],0))

'''
TODO
'''


