class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        k %= len(nums)
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]
                print(nums)
        """
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            prev = nums[start]
            current = start
            while True:
                ahead = (current + k) % n
                nums[ahead], prev = prev, nums[ahead]
                current = ahead
                count += 1
                
                if start == current:
                    break
            start += 1
                
   
                
            
                    
                
        