# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        from collections import deque
        q=deque()
        q.append((root,str(root.val)))
        res=[]
        while q:
            node,val=q.popleft()
            if not node.left and not node.right:
                res.append(val)
            if node.left:
                q.append((node.left,val+"->"+str(node.left.val)))
            if node.right:
                q.append((node.right,val+"->"+str(node.right.val)))
        return res


        