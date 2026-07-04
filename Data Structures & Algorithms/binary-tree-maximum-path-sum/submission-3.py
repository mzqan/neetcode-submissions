# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            # left gain, exclude negaives
            left = max(0, dfs(node.left))

            # right gain, exclude negatives
            right = max(0, dfs(node.right))

            case1 = node.val + left
            case2 = node.val + right

            case3 = node.val + left + right

            # treat split as new contendor
            res = max(res, case3)
            
            # max value given as a "single path", parent path will check "contendors"
            return max(case1, case2)

        dfs(root)
        return res