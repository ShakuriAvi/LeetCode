'''
05\04\24

Second attempt

1019. Next Greater Node In Linked List

list

Medium

https://leetcode.com/problems/next-greater-node-in-linked-list/description/

Accepted
152.3K
Submissions
251.1K
Acceptance Rate
60.7%

Runtime
175
ms
Beats
20.13%
of users with Python3
Memory
18.56
MB
Beats
96.47%
of users with Python3
'''

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: [ListNode]) -> List[int]:
        head = self.replace_list_node(head)
        stack = []
        res = []
        while head:
            while stack and head.val >= stack[-1]:
                stack.pop()

            if len(stack) == 0 or stack[-1] > head.val:
                res.append(0 if len(stack) == 0 else stack[-1])

            stack.append(head.val)
            head = head.next
        return res[::-1]



        pass

    def replace_list_node(self, head: ListNode):
        ptr1 = head
        ptr2 = head.next
        while ptr2:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
        head.next = None
        head = ptr1
        return head



if __name__ == '__main__':
    # [3, 3]
    print(Solution().nextLargerNodes(ListNode(3,ListNode(3))))
    # [2, 7, 4, 3, 5]
    print(Solution().nextLargerNodes(ListNode(2,ListNode(7,ListNode(4,ListNode(3,ListNode(5)))))))
    # [2, 1, 5]
    print(Solution().nextLargerNodes(ListNode(2,ListNode(1,ListNode(5)))))



'''
# [2, 7, 4, 3, 5]
[]
[0]
[0,5]
[0,5

'''