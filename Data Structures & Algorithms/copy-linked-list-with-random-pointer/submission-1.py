"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        curr = head
        dummy = Node(0)
        curr2 = dummy
        while curr:
            curr2.next = Node(curr.val)
            nodes[curr] = curr2.next
            curr2 = curr2.next
            curr = curr.next
        
        curr = head
        curr2 = dummy.next
        while curr:
            curr2.random = nodes[curr.random] if curr.random else None
            curr2 = curr2.next
            curr = curr.next
        
        return dummy.next

        
