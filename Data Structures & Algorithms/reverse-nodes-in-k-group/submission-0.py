# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # keep incrementing i, move fast forward
        # if i != and i % k == 0
        # call reverse from slow to fast
        # elif fast is null, then break
        while True:

            skip = False
            for i in range(k):
                if not fast:
                    skip = True
                    break

                # advance fast for k steps
                fast = fast.next

            if skip or not fast:
                break
        
            # save fast's next, break tie
            temp = fast.next
            fast.next = None

            # remember start of group (to be end)
            tempSlow = slow.next

            # attach after reverse from slow to fast
            slow.next = self.reverse(tempSlow)

            # reattach new end (ex. start) to temp (fast's ex next)
            tempSlow.next = temp

            # update slow, fast
            slow = tempSlow
            fast = slow
        
            if fast == None:
                break
        
        return dummy.next


    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev





