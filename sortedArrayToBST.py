'''
28\06\24

108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Accepted
1.2M
Submissions
1.7M
Acceptance Rate
72.0%

Memory
17.72
MB
Beats
66.25%

Runtime
57
ms
Beats
38.32%

'''
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(nums) - 1)
    def my_sol_sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(root: Optional[TreeNode] ,nums: List[int]):
            len_items = len(nums)
            if len_items == 0:
                return root

            half_items = len_items//2
            val = nums[half_items]

            if root.val > val:
                root.left = TreeNode(val)
                bst(root.left, nums[0:half_items])
                bst(root.left, nums[half_items+1:len_items])
            else:
                root.right = TreeNode(val)
                bst(root.right, nums[0:half_items])
                bst(root.right, nums[half_items+1:len_items])

        len_items = len(nums)
        val = nums[len_items//2]
        root = TreeNode(val)
        bst(root, nums[0:len_items // 2])
        bst(root, nums[len_items // 2 + 1:len_items])
        return root










if __name__ == '__main__':
    sol = Solution()
    sol.sortedArrayToBST([-10,-3,0,5,9])