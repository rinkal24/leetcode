# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        
        while ptr and ptr.next:
            prev = ptr.val
            nextNode = ptr.next.val 
            
            if prev == nextNode:
                
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
            
        return head