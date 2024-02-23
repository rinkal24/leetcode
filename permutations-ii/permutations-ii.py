class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, ctr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in ctr:
                if ctr[num] > 0:
                    ctr[num] -= 1
                    curr.append(num)
                    backtrack(curr, ctr)
                    ctr[num] += 1
                    curr.pop()
                    
        ans = []
        backtrack([], Counter(nums))
        return ans