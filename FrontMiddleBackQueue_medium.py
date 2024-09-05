
class ListNode:
    def __init__(self, val: int, prev = None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class FrontMiddleBackQueue:

    def __init__(self):
        self.counter = 0
        self.head = None
        self.tail = None


    def pushFront(self, val: int) -> None:
        if self.counter == 0:
            self.__first_item_init(val)
            return None

        new_node = ListNode(val, next= self.head)
        self.head.prev = new_node
        self.head = new_node
        self.counter += 1

    def pushMiddle(self, val: int) -> None:
        if self.counter == 0:
            self.__first_item_init(val)

        elif self.counter == 1:
            new_node = ListNode(val, next=self.head)
            self.head = new_node
            self.tail.prev = new_node
            self.counter += 1

        elif self.counter == 2:
            new_node = ListNode(val, prev=self.head, next=self.tail)
            self.head.next = new_node
            self.tail.prev = new_node
            self.counter += 1

        else:
            middle_pos = self.counter // 2 if self.counter % 2 == 0 else self.counter // 2 - 1
            middle_node = self.head
            while middle_node and middle_pos != 0:
                middle_node = middle_node.next
                middle_pos -= 1

            next_item = middle_node.next if middle_node and middle_node.next else None
            prev_item = middle_node if middle_node else None
            new_node = ListNode(val, next=next_item, prev=prev_item)
            if next_item:
                next_item.prev = new_node
            if prev_item:
                prev_item.next = new_node
            self.counter += 1

    def pushBack(self, val: int) -> None:
        if self.counter == 0:
            self.__first_item_init(val)
            return None

        new_node = ListNode(val, prev= self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.counter += 1

    def __first_item_init(self, val):
        self.head = ListNode(val)
        self.tail = self.head
        self.counter += 1

    def popFront(self) -> int:
        res = self.head.val if self.head else -1
        if res != -1:
            self.counter -= 1
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head

        return res

    def popMiddle(self) -> int:
        if self.counter == 0:
            return -1
        middle_pos = self.counter // 2 if self.counter % 2 == 1 else self.counter // 2 - 1
        middle_node = self.head
        while middle_pos != 0:
            middle_node = middle_node.next
            middle_pos -= 1

        res = middle_node.val if middle_node else -1
        if res != -1:
            next_item = middle_node.next if middle_node and middle_node.next else None
            prev_item = middle_node.prev if middle_node and middle_node.prev else None
            if next_item:
                next_item.prev = prev_item
            if prev_item:
                prev_item.next = next_item
        if middle_node == self.head:
            self.head = self.tail

        self.counter -= 1
        return res

    def popBack(self) -> int:
        res = self.tail.val if self.tail else -1
        if res != -1:
            self.counter -= 1
            new_tail = self.tail.prev
            if self.counter != 0:
                new_tail.next = None
                self.tail = new_tail
            else:
                self.tail = self.head = None

        return res

if __name__ == '__main__':
    # Your FrontMiddleBackQueue object will be instantiated and called as such:
    obj = FrontMiddleBackQueue()
    # obj.pushMiddle(1)
    # obj.pushMiddle(2)
    # obj.pushMiddle(3)
    # print(obj.popMiddle())
    # print(obj.popMiddle())
    # print(obj.popMiddle())
    obj.pushFront(1)
    obj.pushBack(2)
    obj.pushMiddle(3)
    obj.pushMiddle(4)
    print(obj.popFront())
    print(obj.popMiddle())
    print(obj.popMiddle())
    print(obj.popBack())
    print(obj.popFront())

    # param_6 = obj.popBack()
    #["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]
    #[[],[1],[2],[3],[4],[],[],[],[],[]]