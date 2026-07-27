# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot:
            left = self.isSameTree(root.left, subRoot.left)
            right = self.isSameTree(root.right, subRoot.right)
            if root.val == subRoot.val:
                return left and right
            return False
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right