class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            if nums[mid - 1] < target and nums[mid] > target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if mid == len(nums) - 1 and nums[mid] < target:
            return len(nums)
        return mid