"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visitedNode = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node in self.visitedNode:
            return self.visitedNode[node]
        
        cloneNode = Node(node.val, [])
        self.visitedNode[node] = cloneNode
        if node.neighbors:
            cloneNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return cloneNode