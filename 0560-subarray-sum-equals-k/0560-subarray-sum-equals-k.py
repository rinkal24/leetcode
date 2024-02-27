class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sum_val = 0
        prefix = {0:1}
        
        for n in nums:
            sum_val += n
            diff = sum_val - k
            
            count += prefix.get(diff, 0)
            prefix[sum_val] = prefix.get(sum_val,0) + 1
        return count