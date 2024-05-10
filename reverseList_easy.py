'''
10\05\24

206. Reverse Linked Listhttps://leetcode.com/problems/reverse-linked-list/description/
Easy

Accepted
4.1M
Submissions
5.4M
Acceptance Rate
76.6%
Memory
17.73
MB
Beats
33.98%
of users with Python3

Runtime
36
ms
Beats
66.47%
of users with Python3
'''

from typing import Optional
# Definition for singly-linked list.
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_l_list(lst: list):
    queue = deque(lst)
    if len(queue) == 0:
        return None
    head = ListNode(queue.popleft())
    node = head
    while queue:
        node.next = ListNode(queue.popleft())
        node = node.next
    return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ptr1 = head
        ptr2 = head.next if head.next else None
        while ptr2:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3

        head.next = None
        return ptr1



if __name__ == '__main__':
    # print(Solution().reverseList(build_l_list([1, 2, 3, 4, 5])))
    print(Solution().reverseList(build_l_list([1,2])))

