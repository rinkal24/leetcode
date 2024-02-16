class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        
        formed = 0
        reqd = len(dict_t)
        lo, hi = 0, 0
        
        window_counts = {}
        ans = float("inf"), None, None
        
        while hi < len(s):
            char = s[hi]
            window_counts[char] = window_counts.get(char,0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            while lo <= hi and formed == reqd:
                char = s[lo]
                if hi - lo + 1 < ans[0]:
                    ans = hi - lo + 1, lo, hi
                    
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -=1
                lo += 1
            hi += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]