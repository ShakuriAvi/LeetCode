'''
06\04\24

102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1224886394/

Binary Tree
medium

Accepted
2.2M
Submissions
3.3M
Acceptance Rate
67.0%

Memory
17.28
MB
Beats
53.05%
of users with Python3

Runtime
30
ms
Beats
97.50%
of users with Python3

'''

from typing import List
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder.pop(0))
    queue = [root]
    while queue:
        node = queue.pop(0)
        if len(preorder) > 0:
            new_node = add_left_child(node, preorder.pop(0))
            if new_node:
                queue.append(new_node)
        if len(preorder) > 0:
            new_node = add_right_child(node, preorder.pop(0))
            if new_node:
                queue.append(new_node)
    return root

def add_right_child( root: TreeNode, val:int)->TreeNode:
    if val:
        newNode = TreeNode(val)
        if not root.right:
            root.right = newNode
    else:
        newNode = None
    return newNode

def add_left_child( root: TreeNode, val:int)->TreeNode:
    if val:
        newNode = TreeNode(val)
        if not root.left:
            root.left = newNode
    else:
        newNode = None
    return newNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[str]]:
        def bfs(root: TreeNode):
            if not root:
                return []
            res = []
            queue = [(root,1)]
            while queue:

                node, layer = queue.pop(0)
                if len(res) != layer:
                    res.append([])
                res[layer-1].append(node.val)
                if node.left:
                    queue.append((node.left,layer+1))
                if node.right:
                    queue.append((node.right,layer+1))

            return res
        return bfs(root)

if __name__ == '__main__':
    print(Solution().levelOrder(buildTree([3,9,20,None,None,15,7])))



