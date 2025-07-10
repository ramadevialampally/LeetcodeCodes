# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        if not root.left and not root.right:
            return [root.val]
        a=[]
        from collections import deque
        q=deque()
        q.append(root)
        while q:
            x=q.popleft()
            a.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m=0
        for k,v in d.items():
            if v>m:
                m=v
        res=[]
        for k,v in d.items():
            if v==m:
                res.append(k)
        return res
          