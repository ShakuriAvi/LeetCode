'''
10\05\24

700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/description/
Binary Tree
Easy

Accepted
857.9K
Submissions
1.1M
Acceptance Rate
79.7%

Memory
18.37
MB
Beats
29.15%
of users with Python3

Runtime
54
ms
Beats
63.69%
of users with Python3
'''

from treeBuilders import from_lst_to_binary_tree
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root.val == val:
                return root

            queue.append(root.left)
            queue.append(root.right)


        return None

if __name__ == '__main__':
    print(Solution().searchBST(from_lst_to_binary_tree([4, 2, 7, 1, 3]),2))

