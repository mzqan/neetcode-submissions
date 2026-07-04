# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        
        def dfs(limit):
            nonlocal preIdx, inIdx
            
            # Base Case 1: If we processed all elements in preorder, we are done
            if preIdx >= len(preorder):
                return None
                
            # Base Case 2: If the current inorder element matches our limit,
            # we have finished constructing this subtree.
            if inIdx < len(inorder) and inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            # Root of this subtree is always the current preorder element
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            # Build left subtree: everything until we hit the current root's value
            root.left = dfs(root.val)
            
            # Build right subtree: everything until we hit the parent's limit
            root.right = dfs(limit)

            return root

        return dfs(float('inf'))