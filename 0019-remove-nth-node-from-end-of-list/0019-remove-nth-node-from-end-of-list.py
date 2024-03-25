# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodeLen = 0
        
        while curr:
            curr = curr.next
            nodeLen += 1
            
        curr = head
        ind = nodeLen - n
        ctr = 0
        prev = ListNode()
        ans = curr if ind !=0 else prev
        firstOne = True if ind == 0 else False
        
        while curr:
            nextNode = curr.next
            if ctr == ind or firstOne:
                prev.next = nextNode
                curr = nextNode
                ctr += 1
                if ind == 0:
                    firstOne = False
                continue
                
            ctr += 1
            prev = curr
            curr = curr.next
      
        return ans if ind != 0 else ans.next