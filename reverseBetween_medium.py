'''
10\05\24

92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/description/medium

Accepted
860.8K
Submissions
1.8M
Acceptance Rate
47.7%

Memory
16.65
MB
Beats
62.27%
of users with Python3

Runtime
32
ms
Beats
76.85%
of users with Python3
'''

from typing import Optional
from collections import deque
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        ptr1 = None
        ptr2 = head
        counter = 1
        while ptr2:
            if counter == left:
                ptr3 = ptr2
                while counter != right:
                    ptr2 = ptr2.next
                    counter += 1

                head_rl = self.reverseList(ptr3, right - left, ptr2.next)
                if ptr1:
                    ptr1.next = head_rl
                else:
                    head = head_rl
                break
            ptr1 = ptr2
            ptr2 = ptr2.next
            counter += 1

        return head

    def reverseList(self, head: Optional[ListNode], iterations, end: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head.next if head.next else None
        count = 0
        while count != iterations:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
            count += 1

        head.next = end
        return ptr1

if __name__ == '__main__':
    # print(Solution().reverseBetween(build_l_list([1, 2, 3, 4, 5]), 2, 4))
    print(Solution().reverseBetween(build_l_list([3,5]), 1, 2))

