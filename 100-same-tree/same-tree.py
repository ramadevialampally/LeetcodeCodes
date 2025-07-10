# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not p and q or (not q and p):
            return False
        from collections import deque
        q1=deque()
        q2=deque()
        q1.append(p)
        q2.append(q)
        
        while q1 and q1:
            a=q1.popleft()
            b=q2.popleft()
            if a.val!=b.val:
                return False
            if a.left or b.left:
                if(a.left and not b.left) or (not a.left and b.left):
                    return False
                if a.left:
                    q1.append(a.left)
                if b.left:
                    q2.append(b.left)
            if a.right or b.right:
                if(a.right and not b.right) or (not a.right and b.right):
                    return False
                if a.right:
                    q1.append(a.right)
                if b.right:
                    q2.append(b.right)
            
        return True
            
                
