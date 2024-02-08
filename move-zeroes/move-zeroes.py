class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroptr = -1
        ptr = 0
        while(ptr < len(nums)):
            if nums[ptr] == 0:
                zeroptr = ptr
                break
            ptr += 1
        ptr = 0
        
        while(ptr < len(nums) and zeroptr >= 0):
            if nums[ptr] == 0 or ptr < zeroptr:
                ptr += 1
                continue
            else:
                nums[zeroptr] = nums[ptr]
                nums[ptr] = 0
                zeroptr += 1
                ptr += 1
        
            