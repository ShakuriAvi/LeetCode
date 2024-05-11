'''
10\05\24

21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

Accepted
4.1M
Submissions
6.4M
Acceptance Rate
64.3%

Memory
16.54
MB
Beats
58.57%
of users with Python3

Runtime
61
ms
Beats
6.59%
of users with Python3
'''


from collections import deque
from typing import Optional
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = ListNode(-1)
        temp = head3
        self.merge(head1, head2, head3)
        print(temp)
        return temp.next




    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode], head3: Optional[ListNode]):
        if not head1 and not head2:
            return None
        if not head1:
            head3.next = head2
            return head2
        if not head2:
            head3.next = head1
            return head1

        if head1.val < head2.val:
            val = head1.val
            head1 = head1.next
        else:
            val = head2.val
            head2 = head2.next
        head3.next = ListNode(val)
        head3 = head3.next
        self.merge(head1, head2, head3)







if __name__ == '__main__':
    print(Solution().mergeTwoLists(build_l_list([1,2,4]), build_l_list([1,3,4])))
