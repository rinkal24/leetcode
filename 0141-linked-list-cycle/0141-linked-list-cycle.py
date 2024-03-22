# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []
        seen = set()
        
        while head:
            if head in arr:
                return True
            arr.append(head)
            head = head.next
        return False