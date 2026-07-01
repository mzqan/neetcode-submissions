# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # add both lists
        # head = 2 -> 4 -> 6 -> None
        # head2 = 8 -> None
        head1, head2 = head, prev
        while head2:
            temp1 = head1.next   # 4 -> 6 -> None
            temp2 = head2.next  # None

            head1.next = head2   # 2 -> 8 -> None
            head2.next = temp1  # 2 -> 8 -> 4 -> 6 -> None
            
            head1 = temp1        # 4 -> 6 -> None
            head2 = temp2       # None
       

    