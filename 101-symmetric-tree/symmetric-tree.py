# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque

        if not root:
            return True

        q = deque()
        q.append((root.left, root.right))

        while q:
            left, right = q.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            # Push mirror children
            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True

            