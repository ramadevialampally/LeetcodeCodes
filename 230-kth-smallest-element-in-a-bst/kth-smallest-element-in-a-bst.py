# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        from collections import deque
        q=deque()
        q.append(root)
        a=[]
        while q:
            b=q.popleft()
            a.append(b.val)
            if b.left:
                q.append(b.left)
            if b.right:
                q.append(b.right)
        a=sorted(a)
        return a[k-1]


