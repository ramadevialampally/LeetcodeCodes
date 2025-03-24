# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def diamater(root):
            if not root:
                return 0
            lh=diamater(root.left)
            rh=diamater(root.right)
            self.res=max(self.res,lh+rh)
            return 1+max(lh,rh)
        diamater(root)
        return self.res


        