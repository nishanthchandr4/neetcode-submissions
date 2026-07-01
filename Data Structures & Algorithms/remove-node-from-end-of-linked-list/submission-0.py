# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        
        if n == 1:
            tail = tail.next
        else:
            temp = tail
            for i in range(n - 2):
                temp = temp.next
            temp.next = temp.next.next
        
        prev = None
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        
        return prev

        
        
        


        
        




        
        

        




        

        

        
        
        