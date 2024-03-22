# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        Q = deque([root]) 
        ans = []
        
        while Q:
            size = len(Q)
            level_ans = []
            for i in range(size):
                node = Q.popleft()
                level_ans.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
            ans.append(sum(level_ans)/size)
        return ans