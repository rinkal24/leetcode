class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        if len(nums) == 1:
            return 0
        
        
        while lo <= hi:
            mid = int((lo + hi) / 2)
            
            if lo == hi:
                if nums[mid] > nums[mid - 1]:
                    return mid
                hi = mid - 1
                lo = 0
            elif nums[mid + 1] < nums[mid] and nums[mid - 1] < nums[mid]:
                return mid
            else:
                lo = mid + 1
                
            
            
            
        return mid
            