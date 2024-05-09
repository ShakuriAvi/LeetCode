'''
06\04\24

919. Complete Binary Tree Inserter

https://leetcode.com/problems/complete-binary-tree-inserter/description/

Binary Tree
medium

Accepted
52.8K
Submissions
80.7K
Acceptance Rate
65.4%

Memory
17.68
MB
Beats
24.17%
of users with Python3

Runtime
239
ms
Beats
5.11%
of users with Python3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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
    class CBTInserter:

        def __init__(self, root: TreeNode):
            self.root = root
            self.last_item_iterator = self.get_last_item(self.root)

        def get_last_item(self,root: TreeNode) -> TreeNode:
            def bfs(root: TreeNode):
                if not root:
                    return []
                queue = [(root)]
                while queue:
                    root = queue.pop(0)
                    if root.left and root.right:
                        queue.append(root.left)
                        queue.append(root.right)
                    else:
                        return root

                return root
            return bfs(root)


        def insert(self, val: int) -> int:
            new_node = TreeNode(val)
            if not self.last_item_iterator.left:
                self.last_item_iterator.left = new_node
            elif not self.last_item_iterator.right:
                self.last_item_iterator.right = new_node

            parent = self.last_item_iterator
            self.last_item_iterator = self.get_last_item(self.root)
            return parent.val

        def get_root(self) -> TreeNode:
            return self.root


if __name__ == '__main__':
# Your CBTInserter object will be instantiated and called as such:
    cbt = Solution().CBTInserter(buildTree([1, 2]))
    print(cbt.insert(3))
    print(cbt.insert(4))
    print(cbt.get_root())
