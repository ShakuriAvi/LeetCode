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
16.56
MB
Beats
45.46%
of users with Python3

Runtime
35
ms
Beats
68.76%
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        def bfs(root: TreeNode):
            if not root:
                return []
            res = [root.val]
            queue = [(root,0)]
            lst_layers = [True]
            while queue:
                node, layer = queue.pop(0)
                if len(lst_layers) <= layer+1:
                    lst_layers.append(False)

                if node.right:
                    queue.append((node.right,layer+1))
                    if not lst_layers[layer+1]:
                        lst_layers[layer+1] = True
                        res.append(node.right.val)

                if node.left:
                    queue.append((node.left,layer+1))
                    if not lst_layers[layer+1]:
                        lst_layers[layer+1] = True
                        res.append(node.left.val)

            return res
        return bfs(root)

if __name__ == '__main__':
    print(Solution().rightSideView(buildTree([1,2,3,None,5,None,4])))