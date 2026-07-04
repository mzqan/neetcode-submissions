# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: curr, left, right
        # inorder: left, curr, right

        # map value to index
        inorderMap = {}
        for i, v in enumerate(inorder):
            inorderMap[v] = i

        pIdx = 0

        def buildFromHalves(lo, hi):
            nonlocal inorderMap, pIdx
           
            if pIdx >= len(preorder):
                return None

            # find idx within inorder
            idx = inorderMap[preorder[pIdx]]

            # if val not within bounds of its parent
            if not (lo <= idx <= hi):
                return None

            # create new node
            node = TreeNode(preorder[pIdx])

            # advance position in preorder
            pIdx += 1

            node.left = buildFromHalves(lo, idx)
            
            node.right =  buildFromHalves(idx+1, hi)
            
            return node

        return buildFromHalves(0, len(inorder))


