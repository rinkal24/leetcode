# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            leftNode = dfs(node1.left, node2.right)
            rightNode = dfs(node1.right, node2.left)
            
            return node1.val == node2.val and leftNode and rightNode
        return dfs(root, root)