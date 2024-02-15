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
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited ={}
        Q = deque([node])
        visited[node] = Node(node.val, [])
        
        while Q:
            n = Q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    Q.append(neighbor)
                    
                visited[n].neighbors.append(visited[neighbor])
                
        return visited[node]