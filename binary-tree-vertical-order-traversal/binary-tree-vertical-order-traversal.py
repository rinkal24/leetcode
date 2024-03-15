# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic_vals = defaultdict(list)
        Q = collections.deque([(root, 0)])
        while Q:
            node, col = Q.popleft()
            
            if node is not None:
                dic_vals[col].append(node.val)
                Q.append((node.left, col - 1))
                Q.append((node.right, col + 1))
                
                
        return [dic_vals[x] for x in sorted(dic_vals.keys())]
            