class Solution:
    def reverseNums(self, nums, start):
        n = len(nums) - 1
        while start < n:
            nums[start], nums[n]= nums[n], nums[start]
            n -= 1
            start += 1
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while i < j and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverseNums(nums, i + 1)