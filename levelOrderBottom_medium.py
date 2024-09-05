'''
28\06\24

107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
Accepted
654.9K
Submissions
1M
Acceptance Rate
63.7%

Memory
16.81
MB
Beats
20.50%


Runtime
34
ms
Beats
78.66%

'''

from typing import Optional, List
from treeBuilders import from_lst_to_binary_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        items = dict()

        if not root:
            return
        def preorder(root: Optional[TreeNode], level):
            if root.left:
                preorder(root.left, level+1)
            if root.right:
                preorder(root.right, level+1)

            if level not in items:
                items[level] = []
            items[level].append(root.val)
        preorder(root, 0)

        curr = max(items.keys())
        for idx in range(curr, -1, -1):
            res.append(items[idx])
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.levelOrderBottom(from_lst_to_binary_tree([3,9,20,None,None,15,7]))
