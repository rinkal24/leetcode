class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        """
        
        maxJump = nums[0]
        prev = maxJump
        if(len(nums) == 1):
            return True
        
        for i in range(len(nums)):
          
            maxJump, prev = max(maxJump, nums[i] + i), maxJump
            if i > prev:
                return False
        
         
        return True
        
      
            
            
            