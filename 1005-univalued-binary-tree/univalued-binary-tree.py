# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
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
        for i in range(1,len(a)):
            if(a[i-1]!=a[i]):
                return False
        return True
        