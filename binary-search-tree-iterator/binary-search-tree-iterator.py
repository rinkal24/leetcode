# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.nodes = []
        self.head = -1
        self.inorderBST(root)
        
    def inorderBST(self, root):
        if not root:
            return
        
        self.inorderBST(root.left)
        self.nodes.append(root.val)
        self.inorderBST(root.right)
        
    def next(self) -> int:
        self.head += 1
        return self.nodes[self.head]
        

    def hasNext(self) -> bool:
        return self.head + 1 < len(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()