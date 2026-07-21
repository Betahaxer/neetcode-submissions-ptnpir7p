# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, root):
        if not root:
            return None
        left = self.invert(root.left) if root.left else None
        right = self.invert(root.right) if root.right else None

        root.left = right
        root.right = left
        return root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)