# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            dummy = head.next
            head.next = None

            while dummy is not None: 
                pointerStore = dummy.next  
                dummy.next = head
                head = dummy
                dummy = pointerStore

            return  head