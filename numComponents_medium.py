'''
26\06\24

817. Linked List Components
https://leetcode.com/problems/linked-list-components/description/

Accepted
94.1K
Submissions
165.6K
Acceptance Rate
56.8%

Memory
20.82
MB
Beats
17.29%

Runtime
72
ms
Beats
85.27%

'''

from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_l_list(lst: list):
    queue = lst
    head = ListNode(queue.pop(0))
    node = head
    while queue:
        node.next = ListNode(queue.pop(0))
        node = node.next
    return head
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        flag = False
        while head:
            curr = head.val

            head = head.next
            if curr in nums and flag is False:
                flag = True
                res += 1
            elif curr not in nums:
                flag = False
        return res





if __name__ == '__main__':
    sol = Solution()
    print(sol.numComponents(build_l_list([0,1,2,3]), [0,1,3]))
    print(sol.numComponents(build_l_list([0,1,2,3,4]), [0,3,1,4]))
    print(sol.numComponents(build_l_list([4,3,1,2,0]), [1,3,0]))
    print(sol.numComponents(build_l_list([0,3,2,4,1]), [3,0,2]))
