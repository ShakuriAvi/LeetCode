'''
26\06\24

1472. Design Browser History
https://leetcode.com/problems/design-browser-history/description/

Accepted
237.8K
Submissions
306.5K
Acceptance Rate
77.6%

Memory
19.00
MB
Beats
74.04%


Runtime
202
ms
Beats
36.37%
'''

class ListNode:
    def __init__(self, val:str, prev = None,  next = None ):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = ListNode(homepage)


    def visit(self, url: str) -> None:
        self.ptr.next = ListNode(url, prev=self.ptr)
        self.ptr = self.ptr.next


    def back(self, steps: int) -> str:
        while steps != 0 and self.ptr.prev:
            self.ptr = self.ptr.prev
            steps -= 1

        return self.ptr.val



    def forward(self, steps: int) -> str:
        while steps != 0 and self.ptr.next:
            self.ptr = self.ptr.next
            steps -= 1

        return self.ptr.val


if __name__ == '__main__':

    # Your BrowserHistory object will be instantiated and called as such:
    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    print(obj.back(1))
    print(obj.back(1))
    print(obj.forward(1))
    obj.visit("linkedin.com")
    print(obj.forward(2))
    print(obj.back(2))
    print(obj.back(7))
