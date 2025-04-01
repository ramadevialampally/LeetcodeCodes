# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
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
        d={}
        for i in range(len(m)):
            d[m[i]]=i
        for i in range(len(m)):
            x=k-m[i]
            if x==m[i] and i==d[x]:
                continue
            elif x in m:
                return True
        return False
        