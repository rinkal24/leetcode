class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lo = self.findRange(nums, target, True)
        if lo == -1:
            return [-1, -1]
        hi = self.findRange(nums, target, False)
        
        return [lo, hi]
        
        
    def findRange(self, nums: List[int], target: int, isFirst: bool) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = int((lo + hi)/2)
            if nums[mid] == target:
                if isFirst:
                    if lo == mid or nums[mid - 1] < target:
                        return mid
                    hi = mid - 1
                else:
                    if hi == mid or nums[mid + 1] > target:
                        return mid
                    lo = mid + 1
                    
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1