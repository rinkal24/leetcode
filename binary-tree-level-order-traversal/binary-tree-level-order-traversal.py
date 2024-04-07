# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        Q = deque([root,])
        ctr = 0
        
        while Q:
            res.append([])
            size = len(Q)
            
            for i in range(size):
                node = Q.popleft()
                res[ctr].append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
            ctr += 1
        return res
        
            