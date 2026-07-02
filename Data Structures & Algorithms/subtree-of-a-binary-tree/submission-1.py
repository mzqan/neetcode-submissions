# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        
        def isSameTree(p, q):
                if not p and not q:
                    return True
                if p and q and p.val == q.val:
                    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                else:
                    return False
            
        def dfs(root):
            if not root:
                return

            if isSameTree(root, subRoot):
                self.res = True
            else:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return  self.res