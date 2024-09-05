'''
26\06\24

Second attempt

234. Palindrome Linked List
LinkedList

Easy

https://leetcode.com/problems/palindrome-linked-list/description/
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

from typing import Optional
from collections import deque
from copy import deepcopy

# Definition for singly-linked list.
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.check_stack_ll_is_equal(self.add_item_to_stack(head), head)

    def replace_direction_ll(self, head: Optional[ListNode]) -> ListNode:
        node1 = None
        while head:
            node2 = head.next
            head.next = node1
            node1 = head
            head = node2
        return node1


    def check_two_ll_is_equal(self, ll1: Optional[ListNode], ll2: Optional[ListNode]) -> bool:
        node1 = ll1
        node2 = ll2
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next

        return True



if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(build_l_list([1,2,2,1])))

