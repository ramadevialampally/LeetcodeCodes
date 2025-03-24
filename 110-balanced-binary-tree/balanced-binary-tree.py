# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if not root:
                return 0
            left=balanced(root.left)
            right=balanced(root.right)
            if(abs(left-right)>1):
                return -1
            if(left==-1 or right==-1):
                return -1
            return 1+max(left,right)
        a=balanced(root)
        if(a!=-1):
            return True
        return False


            