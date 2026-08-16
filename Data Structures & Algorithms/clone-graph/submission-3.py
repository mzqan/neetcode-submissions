"""
# Definition for a Node.
class Node: 
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        mp = {}

        def dfs(node):
            if node.val not in mp:
                mp[node.val] = Node(node.val)
            else:
                return mp[node.val]
            
            mpN = mp[node.val]
            
            if node.neighbors: 
                for n in node.neighbors:
                    (mpN.neighbors).append(dfs(n))
            
            return mp[node.val]

        return dfs(node)

