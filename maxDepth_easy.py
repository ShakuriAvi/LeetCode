'''
11\05\24

104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Accepted
3.1M
Submissions
4.1M
Acceptance Rate
75.4%

Memory
17.58
MB
Beats
84.32%
of users with Python3

Runtime
42
ms
Beats
44.39%
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def inorder(root: Optional[TreeNode], depth):
            nonlocal max_depth
            if root:
                inorder(root.left, depth + 1)
                print(root.val)
                inorder(root.right, depth + 1)

            else:
                max_depth = max(max_depth, depth)

        inorder(root, 0)
        return max_depth





if __name__ == '__main__':
    print(Solution().maxDepth(from_lst_to_binary_tree([3, 9, 20, None, None, 15, 7])))
