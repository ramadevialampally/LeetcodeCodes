# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr=[]
        from collections import deque
        q=deque()
        q.append(root)
        while q:
            x=q.popleft()
            arr.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        s=0
        for i in arr:
            if i>=low and i<=high:
                s+=i
        return s
        