# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def similar(root,currentsum):
            if not root:
                return 0
            currentsum=(currentsum<<1 )| root.val
            if not root.left and not root.right:
                return currentsum
            return similar(root.left,currentsum)+similar(root.right,currentsum)
        return similar(root,0)