# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            nonlocal diameter
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            
            diameter = max(diameter, leftPath + rightPath)
            
            return max(leftPath, rightPath) + 1
        
        dfs(root)
        return diameter
    