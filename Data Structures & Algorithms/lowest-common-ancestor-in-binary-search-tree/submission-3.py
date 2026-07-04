# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        while res != p and res != q:
            if p.val < res.val and q.val < res.val:
                res = res.left
            elif p.val > res.val and q.val > res.val:
                res = res.right
            else:
                break

        return res