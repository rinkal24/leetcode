"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def __init__(self):
        self.visited_dictionary = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        
        if head in self.visited_dictionary:
            return self.visited_dictionary[head]
        
        newNode = Node(head.val, None, None)
        self.visited_dictionary[head] = newNode
        
        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)
        
        return newNode
            
            