class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(len(nums)):
            #print(nums[i])
            #print(nums[i]+i, dp[i-1])
            dp[i] = max(nums[i]+i, dp[i-1])
            #print(dp)
        
            if i > dp[i-1]:
                #print("cant reach")
                return False
        return True
            
            
            
            