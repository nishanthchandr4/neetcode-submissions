# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(-1) # starting node
        cur1 = list1
        cur2 = list2
        cur3 = newList
    
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                #create a new node
                temp = ListNode(cur1.val)
                cur3.next = temp
                cur3 = cur3.next
                #move cur1 to the next node
                cur1 = cur1.next
            else: #cur2 is greater
                #create new node
                temp = ListNode(cur2.val)
                #add the node to the end of newList
                cur3.next = temp
                cur3 = cur3.next
                #move cur2 to the next node
                cur2 = cur2.next
        #add the remaing nodes of the non null linked list to the final list
        if cur1 is None:
            cur3.next = cur2
        if cur2 is None:
            cur3.next = cur1



        return newList.next


            
                
