from typing import List
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
    def isValidBST(self, root: TreeNode) -> bool:
        pass
        def bfs(root):
            pass

if __name__ == '__main__':
    # print(Solution().isValidBST(buildTree([2, 1, 3])))
    # print(Solution().isValidBST(buildTree([5,1,4,None,None,3,6])))
    # print(Solution().isValidBST(buildTree([5,4,6,None,None,3,7])))
    # print(Solution().isValidBST(buildTree([2,2,2])))
    print(Solution().isValidBST(buildTree([32,26,47,19,None,None,56,None,27])))

# TO DO


