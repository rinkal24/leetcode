# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        before = dummy
        
        for i in range(1, left):
            before = before.next
            
        prev = before
        curr = before.next
        
        
        for i in range(left, right + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        before.next.next = curr
        before.next = prev
        
        
        return dummy.next