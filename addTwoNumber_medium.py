'''
19\10\23
2. Add Two Numbers

Linked List
Medium
https://leetcode.com/problems/split-linked-list-in-parts/description/
Acceptance Rate : 41.4%, Submissions : 9.6M,  Accepted: 4M

'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        l3 = self.create_ll(num1 + num2)
        return l3

    def get_num(self, ll):
        node = ll
        res_str = ''
        while node:
            res_str += str(node.val)
            node = node.next

        res = int(res_str[::-1])
        return res

    def create_ll(self, num):
        num_str = str(num)[::-1]
        head = ListNode(num_str[0])
        node = head
        for i in range(1, len(num_str)):
            node.next = ListNode(num_str[i])
            node = node.next

        return head


