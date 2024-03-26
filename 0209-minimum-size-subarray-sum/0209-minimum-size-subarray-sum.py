class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = 0
        total = 0
        minLen = math.inf
        for i in range(len(nums)):
            total += nums[i]
              
            while total >= target:
                minLen = min(minLen, i - start + 1)
                total -= nums[start]
                start += 1
                    
        return minLen if minLen != math.inf else 0