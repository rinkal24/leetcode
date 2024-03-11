# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserial(root, strVal):
            if root is None:
                strVal += 'None,'
            else:
                strVal += str(root.val) + ','
                strVal = rserial(root.left, strVal)
                strVal = rserial(root.right, strVal)
            return strVal
        
        return rserial(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserial(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
            node = TreeNode(l.pop(0))
            node.left = deserial(l)
            node.right = deserial(l)
            return node
        
        data_list = data.split(',')
        return deserial(data_list)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))