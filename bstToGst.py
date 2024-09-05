from treeBuilders import from_lst_to_binary_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []
        last_val = 0
        def postorder(node):
            nonlocal last_val

            if node.right:
                postorder(node.right)

            if node.val:
                node.val += last_val
                last_val = node.val - last_val
            arr.append(node.val)
            if node.left:
                postorder(node.left)

        postorder(root)
        print(arr)




if __name__ == '__main__':
    print(Solution().bstToGst(from_lst_to_binary_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])))

