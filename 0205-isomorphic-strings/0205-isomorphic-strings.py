class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ctr_s = Counter(s)
        ctr_t = Counter(t)
        d = {}
        
        for i in range(len(s)):
            
            if s[i] not in d:
                d[s[i]] = t[i]
            if ctr_s[s[i]] != ctr_t[t[i]] or d[s[i]] != t[i]:
                return False
            
        return True