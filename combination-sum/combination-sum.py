class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, curr, ind):
            if remain == 0:
                res.append(list(curr))
                curr = []
                return 
            
            if remain < 0:
                return
            
            for i in range(ind, len(candidates)):
                curr.append(candidates[i])
                backtrack(remain - candidates[i], curr, i)
                curr.pop()
                
        res = []
        backtrack(target, [], 0)
        return res