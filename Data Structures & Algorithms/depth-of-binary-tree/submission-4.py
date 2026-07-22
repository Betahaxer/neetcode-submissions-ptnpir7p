# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def dfs(self, root, depth):
    #     if not root:
    #         return depth
    #     left = right = depth
    #     if root.left:
    #         left = self.dfs(root.left, depth + 1)
    #     if root.right:
    #         right = self.dfs(root.right, depth + 1)
        
    #     return max(left, right)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res