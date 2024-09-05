'''
28\06\24
second attempt
538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/description/
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        add_val = 0
        while queue:
            node = queue.pop()
            while node:
                node = node.right
                queue.append(node)
            node.val += add_val
            add_val += node.val
            visit.add(node)
            if node.left:
                queue.append(node.left)

        return root


if __name__ == '__main__':
    sol = Solution()
    sol.convertBST(from_lst_to_binary_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]))
