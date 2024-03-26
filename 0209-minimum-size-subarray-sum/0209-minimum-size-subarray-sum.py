class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = 0
        total = 0
        minLen = math.inf
        for i in range(len(nums)):
            total += nums[i]
            if total >= target:
                #print(total, start, i)
                minLen = min(minLen, i - start + 1)
                while total >= target:
                    minLen = min(minLen, i - start + 1)
                    total -= nums[start]
                    start += 1
                    #print('here', start, total)
        #print(start)
        return minLen if minLen != math.inf else 0