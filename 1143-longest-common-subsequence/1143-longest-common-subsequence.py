class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize = None)
        def dfs(ind1, ind2):
            if ind1 == len(text1) or ind2 == len(text2):
                return 0
            
            if text1[ind1] == text2[ind2]:
                return 1 + dfs(ind1 + 1, ind2 + 1)
            
            
            return max(dfs(ind1 + 1, ind2), dfs(ind1, ind2 + 1))
                
    
        return dfs(0, 0)