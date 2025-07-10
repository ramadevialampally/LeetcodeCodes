# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        a=[]
        from collections import deque
        q=deque()
        q.append(root)
        while  q:
            m=len(q)
            for i in range(m):
                b=q.popleft()
                b.left,b.right=b.right,b.left
                if b.right:
                    q.append(b.right)
                if b.left:
                    q.append(b.left)
        return root
                