# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0, True]

            leftHeight, leftBalanced = dfs(root.left)
            rightHeight, rightBalanced = dfs(root.right)

            balanced = leftBalanced and rightBalanced and abs(leftHeight-rightHeight) <= 1
            return [max(leftHeight, rightHeight) + 1, balanced]

        return dfs(root)[1]