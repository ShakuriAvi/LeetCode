'''
11\05\24

404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/description/Easy

Accepted
617.2K
Submissions
1M
Acceptance Rate
60.6%

Memory
16.73
MB
Beats
49.05%
of users with Python3

Runtime
39
ms
Beats
35.39%
of users with Python3
'''

from typing import Optional
from treeBuilders import from_lst_to_binary_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def inorder(root: Optional[TreeNode]):
            nonlocal res
            if root:
                if root.left and (not root.left.left and not root.left.right):
                    res += root.left.val
                inorder(root.left)
                inorder(root.right)

        inorder(root)
        return res

if __name__ == '__main__':
    print(Solution().sumOfLeftLeaves(from_lst_to_binary_tree([1,2,3,4,5])))

