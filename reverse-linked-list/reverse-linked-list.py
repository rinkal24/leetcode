# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ListNode(0)
        ans = list1
        dummy = head
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
            
        ptr = len(nums) - 1
        while ptr >= 0:
            newNode = ListNode(nums[ptr])
            list1.next = newNode
            list1 = list1.next
            ptr -= 1
            
        return ans.next