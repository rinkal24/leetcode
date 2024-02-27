class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
     
        maxLen = 0
        start = 0
        ctr = collections.Counter() ###Counter(s[start:i + 1])
        
        for i in range(len(s)):
            ctr[s[i]] += 1
            if len(ctr) <= k:
                maxLen = max(maxLen, i - start + 1)
            else:
                ctr[s[start]] -= 1
                if ctr[s[start]] == 0:
                    del ctr[s[start]]
                start += 1
            
            
        return maxLen  if k > 0 else 0