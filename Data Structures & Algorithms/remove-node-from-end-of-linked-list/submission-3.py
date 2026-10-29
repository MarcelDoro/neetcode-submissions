# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        count_help = head
        while count_help != None:
            count += 1
            count_help = count_help.next
        
        print(count)
        if count == 1:
            return None
        if count == n:
            return head.next

        move = count - n
        move_help = head
        while move > 1: # 1 bc we want to be before it
            move_help = move_help.next
            move -= 1

        move_help.next = move_help.next.next

        return head