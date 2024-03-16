# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurseTree(node):
            if not node:
                return False
            
            left = recurseTree(node.left)
            right = recurseTree(node.right)
            
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.ans = node
                
            return mid or left or right
        
        recurseTree(root)
        return self.ans