class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.caches = {}

        self.end = ListNode(0, -1)
        self.start = ListNode(0, -1)  

        self.start.next = self.end  
        self.end.prev = self.start  
        

    def get(self, key: int) -> int:
        if key in self.caches:
            self.caches[key].prev.next = self.caches[key].next
            self.caches[key].next.prev = self.caches[key].prev
            
            self.start.next.prev = self.caches[key]
            self.caches[key].next = self.start.next
            self.caches[key].prev = self.start
            self.start.next = self.caches[key]

            return self.caches[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            self.caches[key].val = value

            self.caches[key].prev.next = self.caches[key].next
            self.caches[key].next.prev = self.caches[key].prev
            
            self.start.next.prev = self.caches[key]
            self.caches[key].next = self.start.next
            self.caches[key].prev = self.start
            self.start.next = self.caches[key]

        else:
            newNode = ListNode(value, key)
            self.start.next.prev = newNode
            newNode.next = self.start.next
            newNode.prev = self.start
            self.start.next = newNode
            self.caches[key] = newNode
            if len(self.caches) > self.maxSize:
                self.caches.pop(self.end.prev.key)
                self.end.prev = self.end.prev.prev
                self.end.prev.next = self.end
            


        
