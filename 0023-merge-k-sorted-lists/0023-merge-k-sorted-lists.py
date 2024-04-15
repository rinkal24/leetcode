# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []
        for i in lists:
            head = i
            while head:
                res.append(head.val)
                head = head.next
       
        res.sort()
        head = ListNode(0)
        ptr = head
        
        for i in res:
            newNode = ListNode(i)
            ptr.next = newNode
            ptr = ptr.next
        return head.next
            