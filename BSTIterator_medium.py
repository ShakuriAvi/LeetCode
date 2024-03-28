'''
06\02\24

173. Binary Search Tree Iterator

Binary Tree

Medium

https://leetcode.com/problems/binary-search-tree-iterator/description/

"Accepted
750.4K
Submissions
1M
Acceptance Rate
71.5%"

"Memory Beats68.13%of users with Python,Run time Beats
8.63%
of users with Python"

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.sorted_arr = [root.val]
        self.create_Tree(root)
        print(self.sorted_arr)

    def create_Tree(self, root):
        queue = [(root, 0)]
        while queue:
            root, idx = queue.pop()
            i = 1
            if root.left:
                temp = root.left
                self.sorted_arr.insert(idx, temp.val)
                queue.append((temp, idx))
                i += 1
            if root.right:
                temp = root.right
                self.sorted_arr.insert(idx + i, temp.val)
                queue.append((temp, idx + i))

    def next(self):
        """
        :rtype: int
        """
        return self.sorted_arr.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.sorted_arr) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


'''
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.values = self.getValues(root)
    
    def getValues(self, root: Optional[TreeNode]):
        values = []

        def dfs(node):
            if node:
                dfs(node.left)
                values.append(node.val)
                dfs(node.right)

        dfs(root)

        return values


    def next(self) -> int:
        node = self.values[self.idx]
        self.idx += 1

        return node

    def hasNext(self) -> bool:
        return self.idx < len(self.values)

'''