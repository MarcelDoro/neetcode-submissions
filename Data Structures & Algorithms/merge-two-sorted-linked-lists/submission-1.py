# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if l1 == None and l2 == None:
            return None
            
        head = ListNode()
        res = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.val = l1.val
                l1 = l1.next
            else:
                head.val = l2.val
                l2 = l2.next

            head.next = ListNode()
            head = head.next
        
        
        while l1 != None:
            head.val = l1.val
            l1 = l1.next
            if l1 != None:
                head.next = ListNode()
                head = head.next

        while l2 != None:
            head.val = l2.val
            l2 = l2.next
            if l2 != None:
                head.next = ListNode()
                head = head.next

        return res
            
        