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
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 1
        while stack:
            cur = stack.pop()
            depth = max(cur[1], depth)
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                stack.append((cur[0].right, cur[1] + 1))
        return depth