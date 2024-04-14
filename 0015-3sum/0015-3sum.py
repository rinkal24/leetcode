class Solution:
    def twoSum(self, nums, i, res):
        visited = set()
        j = i+1
        while j < len(nums):
            target = 0-nums[i]
            if target - nums[j] in visited:
                res.append([nums[i], nums[j], target - nums[j]])
                while j+1< len(nums) and nums[j] == nums[j+1]:
                    j += 1
            visited.add(nums[j])
            j+=1 
        
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res  = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break 
            if i==0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res