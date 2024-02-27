class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
     
        maxLen = 0
        start = 0
        
        for i in range(len(s)):
            ctr = Counter(s[start:i + 1])
            if len(ctr) <= k:
                maxLen = max(maxLen, i - start)
            else:
                ctr[s[start]] -= 1
                if ctr[s[start]] == 0:
                    del ctr[s[start]]
                start += 1
            
            
        return maxLen + 1 if k > 0 else 0