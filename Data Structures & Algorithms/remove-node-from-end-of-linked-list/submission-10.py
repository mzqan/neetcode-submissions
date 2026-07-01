# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        slow = fast = head
        for i in range(n):
            fast = fast.next
        
        prev = dummy
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # remove slow
        prev.next = slow.next
        
        

        return dummy.next
