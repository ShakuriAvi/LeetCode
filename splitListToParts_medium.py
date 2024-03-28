'''
18\10\23
725.Split Linked List in Parts
Linked List
Medium
https://leetcode.com/problems/split-linked-list-in-parts/description/

Acceptance Rate : 63.8%, Submissions : 291.1K,  Accepted: 185.7K


'''

from math import floor

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        length_ll = 0
        node = head
        while node is not None:
            length_ll+=1
            node = node.next

        arr = []
        node = head
        if length_ll<k:
            for i in range(0,k):
                prev = node
                if node:
                    curr = node.next
                    prev.next = None
                else:
                    curr = None
                node = curr
                arr.append(prev)
            return arr

        rest = length_ll%k
        end = int(floor(length_ll/k))
        for i in range(0,k):
            t=1
            first = node
            while t < end and node:
                node = node.next
                t+=1
            if rest > 0:
                node = node.next
                rest-=1

            if node is not None:
                prev = node
                curr = node.next
                prev.next = None
            else:
                curr = None
            node = curr
            arr.append(first)

        return arr

'''
"class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=l1
        last=0
        carry=ListNode()
        while l1 and l2:
            temp=l1.val+l2.val+carry.val
            carry.val=temp//10
            l1.val=temp%10
            last=l1
            l1=l1.next
            l2=l2.next
        if l2: #if l2 has more nodes than l1
            last.next=l2
            l1=l2
        while l1 and carry.val:
            temp=l1.val+carry.val
            carry.val=temp//10
            l1.val=temp%10
            last=l1
            l1=l1.next
        if carry.val:
            last.next=carry
        return res"



'''