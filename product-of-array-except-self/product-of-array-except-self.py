class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev =[1 for i in nums]
        ahead =[1 for i in nums]
        
        if len(nums) == 1:
            return nums
        for i in range(1, len(nums)):
            prev[i] = prev[i - 1] * nums[i - 1]
            
        ptr = len(nums) - 2
        while(ptr >= 0):
            ahead[ptr] = ahead[ptr + 1] * nums[ptr + 1]
            ptr -= 1
            
        for i in range(len(nums)):
            nums[i] = prev[i] * ahead[i]
        return nums