class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if(len(nums) == 1):
            return True
        
        for i in range(len(nums)):
          
            dp[i] = max(dp[i - 1], nums[i] + i)
            if i > dp[i - 1]:
                return False
        
         
        return True
        
        """
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
        """
            
            
            