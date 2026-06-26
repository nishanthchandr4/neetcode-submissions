# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next #the second half
        slow.next = None
        
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        tail = prev #renaming just to make it easier to understand

        while tail:
            temp = head.next
            temp1 = tail.next

            head.next = tail
            tail.next = temp

            tail = temp1
            head = temp

        

        
        