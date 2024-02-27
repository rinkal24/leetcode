class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
     
        maxLen = 0
        ctr = collections.Counter() 
        
        for i in range(len(s)):
            ctr[s[i]] += 1
            if len(ctr) <= k:
                maxLen += 1
            else:
                ctr[s[i - maxLen]] -= 1
                if ctr[s[i - maxLen]] == 0:
                    del ctr[s[i - maxLen]]
            
            
        return maxLen 