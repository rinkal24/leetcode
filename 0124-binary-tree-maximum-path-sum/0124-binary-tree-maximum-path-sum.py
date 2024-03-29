# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -math.inf
        
        def dfs(node):
            if not node:
                return 0
            
            nonlocal max_path
            gain_from_left = max(dfs(node.left), 0)
            gain_from_right = max(dfs(node.right), 0)
            
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            
            return max(gain_from_left + node.val, gain_from_right + node.val)
        
        dfs(root)
        return max_path