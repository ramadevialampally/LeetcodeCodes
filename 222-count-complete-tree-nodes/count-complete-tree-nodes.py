# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        q=deque()
        q.append(root)
        c=[]
        while q:
            a=q.popleft()
            c.append(a.val)
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
        return len(c)

        