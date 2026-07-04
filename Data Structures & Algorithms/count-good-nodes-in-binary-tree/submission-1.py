# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, largest):
            if node.val >= largest:
                self.res += 1
                largest = node.val

            if node.left:
                dfs(node.left, largest)
            if node.right:
                dfs(node.right, largest)
        
        dfs(root, float('-inf'))

        return self.res