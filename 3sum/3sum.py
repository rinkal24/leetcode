class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dupes = set(), set()
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes.add(nums[i])
                
                for j in range(i + 1, len(nums)):
                    comp = - nums[i] - nums[j]
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted((nums[i], nums[j], comp))))
                    
                    seen[nums[j]] = i
        return res