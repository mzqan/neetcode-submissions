# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def heightOfTree(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = heightOfTree(root.left)
            right = heightOfTree(root.right)
            self.res = max(self.res, left + right)

            return max(left, right) + 1

        heightOfTree(root)
        return self.res
    

