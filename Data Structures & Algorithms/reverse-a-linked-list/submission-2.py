# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        w1 = head
        w2 = w1.next
        w3 = w2.next
        w1.next = None
        while w3 != None:
            w2.next = w1
            w1 = w2
            w2 = w3
            w3 = w3.next

        w2.next = w1
        return w2