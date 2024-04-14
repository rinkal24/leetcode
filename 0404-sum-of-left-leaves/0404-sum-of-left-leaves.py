# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            nonlocal ans
            if not node.left and not node.right:
                if is_left:
                    ans += node.val
                return 
            
            if node.left:
                dfs(node.left, True)
                
            if node.right:
                dfs(node.right, False)
            return
        
        ans=0
        
        dfs(root, False)
        return ans