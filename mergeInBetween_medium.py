'''
1669. Merge In Between Linked Lists
Linked List
Medium
https://leetcode.com/problems/merge-in-between-linked-lists/description/

Accepted
83.1K
Submissions
114.2K
Acceptance Rate
72.8%

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr_lst1 = list1
        prev = None
        count = 0
        while count != a:
            count += 1
            prev = curr_lst1
            curr_lst1 = curr_lst1.next
        curr_lst2 = list2
        prev.next = curr_lst2
        while count != b:
            count += 1
            curr_lst1 = curr_lst1.next
        while curr_lst2.next != None:
            curr_lst2 = curr_lst2.next

        curr_lst2.next = curr_lst1.next
        return list1

        # Definition for singly-linked list.
