class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, ind, curr):
            
            if remain == 0:
                res.append(list(curr))
                curr = []
                return None
            
            if remain < 0:
                return 
            
            for i in range(ind, len(candidates)):
                curr.append(candidates[i])
                #print(curr)
                backtrack(remain - candidates[i], i, curr)
                curr.pop()
            
        res = []
        backtrack(target ,0, [])
        return res
            