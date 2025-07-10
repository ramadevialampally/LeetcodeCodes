# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        from collections import deque
        q=deque()
        q.append((root,root.val))
        while q:

            node,val=q.popleft()
            if not node.left and not node.right and targetSum==val:
                return True
            if node.left:
                q.append((node.left,val+node.left.val))
            if node.right:
                q.append((node.right,val+node.right.val))
        return False
            

