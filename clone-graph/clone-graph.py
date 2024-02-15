"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        
        cloneNode = Node(node.val, [])
        self.visited[node] = cloneNode
        
        if node.neighbors:
            cloneNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return cloneNode
        
        