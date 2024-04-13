class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m = len(multipliers)
        n = len(nums)
        
        visited = {}
        
        def helper(op, left):
            if op == m:
                return 0
            
            if (op, left) in visited:
                return visited[(op, left)]
            
            l = nums[left] * multipliers[op] + helper(op + 1, left + 1)
            r = nums[(n - 1) - (op - left)] * multipliers[op] + helper(op + 1, left)
            
            visited[(op, left)] = max(l, r)
            
            return visited[(op, left)]
        
        return helper(0, 0)