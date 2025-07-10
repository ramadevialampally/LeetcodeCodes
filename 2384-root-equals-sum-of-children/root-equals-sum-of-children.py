# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        a=root
        leftval=0
        rightval=0
        if a.left:
            leftval=a.left.val
        if a.right:
            rightval=a.right.val
        if(a.val==(leftval+rightval)):
            return True
        return False
            
        