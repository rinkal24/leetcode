class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        limit = len(nums) // 3
        ctr = 1
        res = []
        nums.sort()
        
        
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1] and nums[i] not in res:
                    ctr += 1
                elif nums[i] != nums[i - 1]:
                    ctr = 1
            if ctr > limit and nums[i] not in res:
                res.append(nums[i])
                
        if not res and len(nums) == 1: 
            return nums
        return res