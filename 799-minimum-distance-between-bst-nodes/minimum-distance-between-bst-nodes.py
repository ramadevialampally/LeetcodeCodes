# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        m=[]
        from collections import deque
        q=deque()
        q.append(root)
        while q:
            x=q.popleft()
            m.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        v=float('inf')
        m=sorted(m)
        for i in range(1,len(m)):
            r=m[i]-m[i-1]
            v=min(v,r)
        return v
        