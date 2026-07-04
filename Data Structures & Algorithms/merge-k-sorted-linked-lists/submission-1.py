# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while True:
            toAdd = [float('inf'), None]
            for i, l in enumerate(lists):
                if l and l.val < toAdd[0]:
                    toAdd = [l.val, i]
            
            if toAdd[1] == None:
                break
            
            # get node in list
            node = lists[toAdd[1]]

            # add to our result
            curr.next = node

            # advance list in lists
            lists[toAdd[1]] = node.next
            # remove tie
            node.next = None

            # advance our result
            curr = curr.next

        return dummy.next
            