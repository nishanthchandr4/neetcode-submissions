class ListNode:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0
        
    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        
        dummy = self.head.next
        for i in range(index):
            dummy = dummy.next

        return dummy.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)

        temp = self.head.next
        self.head.next = newNode
        temp.prev = newNode
        newNode.prev = self.head
        newNode.next = temp

        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        temp = self.tail.prev
        temp.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = temp  

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.length:
            return
        
        dummy = self.head.next
        for i in range(index):
            dummy = dummy.next
        
        temp = dummy.prev
        newNode = ListNode(val)

        temp.next = newNode
        dummy.prev = newNode
        newNode.next = dummy
        newNode.prev = temp

        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        
        dummy = self.head.next
        for i in range(index):
            dummy = dummy.next
        
        prev = dummy.prev
        nextt = dummy.next

        prev.next = nextt
        nextt.prev = prev

        self.length -= 1
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)