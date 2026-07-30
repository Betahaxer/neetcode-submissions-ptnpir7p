# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if root.val == p.val or root.val == q.val:
        #     return root
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # return root

        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == p.val or node.val == q.val:
                return node
            if node.val < p.val and node.val < q.val:
                stack.append(node.right)
            elif node.val > p.val and node.val > q.val:
                stack.append(node.left)
            else:
                return node