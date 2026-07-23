# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        
        def maxDepth(root):
            nonlocal best
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            best = max(best, left + right)
            return 1 + max(left, right)
        maxDepth(root)
        return best
