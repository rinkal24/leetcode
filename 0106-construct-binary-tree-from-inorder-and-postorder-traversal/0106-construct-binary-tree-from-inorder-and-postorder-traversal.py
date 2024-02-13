# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            postorder_index -= 1
            
            root.right = array_to_tree(inorder_index_map[root_val] + 1, right)
            root.left = array_to_tree(left, inorder_index_map[root_val] - 1)
            
            
            return root
        
        postorder_index = len(postorder) - 1
        inorder_index_map = {}
        for ind, val in enumerate(inorder):
            inorder_index_map[val] = ind
            
        return array_to_tree(0, postorder_index)