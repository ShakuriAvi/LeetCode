'''
19\10\23
23. Merge k Sorted Lists
Linked List
HARD
https://leetcode.com/problems/merge-k-sorted-lists/
Acceptance Rate : 51.1%, Submissions : 3.5M,  Accepted: 1.8M

'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        head = ListNode(-100000)
        for ll in lists:
            node = head
            node_ll = ll
            while node_ll:
                prev = node
                curr = node.next
                if not curr or node_ll.val < curr.val:
                    new_node = ListNode(node_ll.val,curr)
                    prev.next = new_node
                    node_ll = node_ll.next
                node = node.next
        head =head.next
        return head

'''
"# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self,lists:List[Optional[ListNode]])->Optional[ListNode]:
        values,head,pointer=[],None,None
        for l in lists:
            while l:
                heappush(values,l.val)
                l=l.next

        while values:
            if head is None:
                head=ListNode(heappop(values))
                pointer=head

            else:
                pointer.next=ListNode(heappop(values))
                pointer=pointer.next

        return head             

'''