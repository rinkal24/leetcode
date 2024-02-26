class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
      
        ns = len(s)
        nt = len(t)
        
        if ns > nt:
            return self.isOneEditDistance(t,s)
            
        if nt - ns > 1:
            return False
        
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt: # Delete the mismtach single character in s to match t
                    return s[i + 1:] == t[i + 1:]
                else: #Delete this 1 char from s to make it equal to t
                    return s[i:] == t[i + 1:]
                
        return ns + 1 == nt
                
                
       
        