# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if not root:
            return (0, True)

        leftHeight, leftBalanced = self.getHeight(root.left)
        rightHeight, rightBalanced = self.getHeight(root.right)
        
        if not leftBalanced or not rightBalanced:
            return (0, False)

        if abs(leftHeight - rightHeight) <= 1:
            return (1 + max(leftHeight, rightHeight), True)
        return (1 + max(leftHeight, rightHeight), False)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        rootHeight, rootBalanced = self.getHeight(root)
        return rootBalanced