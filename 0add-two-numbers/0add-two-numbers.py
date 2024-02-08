# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        carry = 0
        while l1 is not None and l2 is not None:
            ans.val = l1.val + l2.val + carry
            num = int(ans.val / 10)
            carry = num if num > 0 else 0
            ans.val = ans.val % 10
            if l1.next is not None and l2.next is not None:
                ans.next = ListNode()
                ans = ans.next

            l1 = l1.next
            l2 = l2.next 
            
        while l1 is not None:
            ans.next = ListNode()
            ans = ans.next
            ans.val = l1.val + carry
            num = int(ans.val / 10)
            carry = num if num > 0 else 0
            ans.val = ans.val % 10
            
            l1 = l1.next
            
        while l2 is not None:
            ans.next = ListNode()
            ans = ans.next
            ans.val = l2.val + carry
            num = int(ans.val / 10)
            carry = num if num > 0 else 0
            ans.val = ans.val % 10
            
            l2 = l2.next
        if carry > 0:
            ans.next = ListNode()
            ans = ans.next
            ans.val = carry
            
        return head