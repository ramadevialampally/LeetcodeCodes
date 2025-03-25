# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q=deque()
        q.append([root,None])
        while q:
            size=len(q)
            parentx=None
            parenty=None
            for i in range(size):
                node,parent=q.popleft()
                if node.val==x:
                    parentx=parent
                if node.val==y:
                        parenty=parent
                if node.left:
                    q.append([node.left,node])
                if node.right:
                    q.append([node.right,node])
            if parentx and parenty:
                return parentx!=parenty
            if parentx or parenty:
                return False
        return False

            
        
            
        