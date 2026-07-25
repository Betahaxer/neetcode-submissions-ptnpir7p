# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def getHeight(self, root):
    #     if not root:
    #         return (0, True)

    #     leftHeight, leftBalanced = self.getHeight(root.left)
    #     rightHeight, rightBalanced = self.getHeight(root.right)
        
    #     if not leftBalanced or not rightBalanced:
    #         return (0, False)

    #     if abs(leftHeight - rightHeight) <= 1:
    #         return (1 + max(leftHeight, rightHeight), True)
    #     return (1 + max(leftHeight, rightHeight), False)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # rootHeight, rootBalanced = self.getHeight(root)
        # return rootBalanced
        if not root:
            return True
        stack = [root]
        mp = {None: (0, True)}

        while stack:
            node = stack[-1]
            if node.left is not None and node.left not in mp:
                stack.append(node.left)
            elif node.right is not None and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftBalanced = mp[node.left]
                rightHeight, rightBalanced = mp[node.right]
                curHeight = 1 + max(leftHeight, rightHeight)
                if not leftBalanced or not rightBalanced:
                    mp[node] = (curHeight, False)
                elif abs(leftHeight - rightHeight) <= 1:
                    mp[node] = (curHeight, True)
                else:
                    mp[node] = (curHeight, False)

        return mp[root][1]
