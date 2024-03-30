class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        sumVal = 0
        for i in range(maxNum + 1):
            sumVal += i
            
        for i in nums:
            sumVal -= i
           
        return sumVal if maxNum == len(nums) else maxNum + 1