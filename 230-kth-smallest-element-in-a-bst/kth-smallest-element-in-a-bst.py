# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque
        q=deque()
        q.append(root)
        a=[]
        while q:
            x=q.popleft()
            a.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        a=sorted(a)
        return a[k-1]

        