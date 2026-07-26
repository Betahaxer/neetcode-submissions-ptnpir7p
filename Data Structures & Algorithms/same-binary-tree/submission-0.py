# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not (root1 and root2) or root1.val != root2.val:
            return False
        left = self.isSame(root1.left, root2.left)
        right = self.isSame(root1.right, root2.right)
        return left and right
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSame(p, q)