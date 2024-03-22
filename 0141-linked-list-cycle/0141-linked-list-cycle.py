# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = set()
        
        while head:
            if head in arr:
                return True
            arr.add(head)
            head = head.next
        return False