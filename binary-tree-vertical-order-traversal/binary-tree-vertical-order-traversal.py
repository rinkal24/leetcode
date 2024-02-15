# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        colTable = defaultdict(list)
        minCol = maxCol = 0
        
        Q = deque([(root, 0)])
        
        while Q:
            node, col = Q.popleft()
            
            if node is not None:
                colTable[col].append(node.val)
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                
                Q.append((node.left, col - 1))
                Q.append((node.right, col + 1))
                
        return [colTable[x] for x in range(minCol, maxCol + 1)]