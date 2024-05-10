'''
10\05\24

1305. All Elements in Two Binary Search Trees
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/submissions/1254388160/Binary Tree
Easy

Accepted
214.7K
Submissions
269.1K
Acceptance Rate
79.8%

Memory
20.52
MB
Beats
17.26%
of users with Python3

Runtime
228
ms
Beats
16.67%
of users with Python3
'''

from treeBuilders import from_lst_to_binary_tree
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst1 = []
        lst2 = []
        def inorder(root:TreeNode, lst: list):
            if root:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)

        inorder(root1, lst1)
        inorder(root2, lst2)

        def merge_two_list(lst1: list, lst2: list) -> List[int]:
            lst_res = []
            while len(lst1) > 0 and len(lst2) > 0:
                if lst1[0] < lst2[0]:
                    lst_res.append(lst1.pop(0))
                elif lst1[0] > lst2[0]:
                    lst_res.append(lst2.pop(0))
                else:
                    lst_res.append(lst1.pop(0))
                    lst_res.append(lst2.pop(0))

            while len(lst1) > 0:
                lst_res.append(lst1.pop(0))

            while len(lst2) > 0:
                lst_res.append(lst2.pop(0))

            return lst_res

        return merge_two_list(lst1, lst2)






if __name__ == '__main__':
    # print(Solution().getAllElements(from_lst_to_binary_tree([2,1,4]),from_lst_to_binary_tree([1,0,3])))

    print(Solution().getAllElements(from_lst_to_binary_tree([5,1,7,0,2]), from_lst_to_binary_tree([])))
