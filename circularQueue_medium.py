'''
05\04\24

622. Design Circular Queue
list

Medium

https://leetcode.com/problems/design-circular-queue/description/

Accepted
308.4K
Submissions
600.1K
Acceptance Rate
51.4%

Runtime
86
ms
Beats
5.54%
of users with Python3

Memory
17.16
MB
Beats
72.36%
of users with Python3
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = k - 1
        self.size = k
        self.arr = [-1] * self.size

    def enQueue(self, value: int) -> bool:
        position = (self.rear + 1) % self.size
        if self.arr[position] != -1:
            return False

        self.arr[position] = value
        self.rear = position
        return True


    def deQueue(self) -> bool:
        position = self.front % self.size
        if self.arr[position] == -1:
            return False
        self.arr[position] = -1
        self.front += 1
        return True



    def Front(self) -> int:
        position = self.front % self.size
        return self.arr[position]


    def Rear(self) -> int:
        position = (self.rear) % self.size
        return self.arr[position]


    def isEmpty(self) -> bool:
        return max([item for item in self.arr]) == -1


    def isFull(self) -> bool:
        return min([item for item in self.arr]) != -1

if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())
