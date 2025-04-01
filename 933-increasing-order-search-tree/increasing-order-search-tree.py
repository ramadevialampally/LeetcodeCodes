# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        a=sorted(a)
        root=TreeNode(a[0])
        temp=root
        for i in range(1,len(a)):
            v=TreeNode(a[i])
            temp.right=v
            temp=temp.right
        return root
        