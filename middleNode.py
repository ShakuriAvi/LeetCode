'''
10\05\24

2379. Minimum Recolors to Get K Consecutive Black Blocks

https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

LinkedList
Easy

Accepted
1.9M
Submissions
2.4M
Acceptance Rate
78.5%

Memory
16.56
MB
Beats
31.32%
of users with Python3

Runtime
35
ms
Beats
54.17%
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
    head = ListNode(queue.popleft())
    node = head
    while queue:
        node.next = ListNode(queue.popleft())
        node = node.next
    return head


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        if ptr1:
            if ptr1.next:
                ptr2 = head.next
                count = 2
            else:
                return ptr1
        else:
            return None

        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            count += 1
            if ptr2.next:
                ptr2 = ptr2.next
                count += 1

        return ptr1 if count % 2 == 1 else ptr1.next



'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer
'''
if __name__ == '__main__':
    print(Solution().middleNode(build_l_list([1, 2, 3, 4])))
