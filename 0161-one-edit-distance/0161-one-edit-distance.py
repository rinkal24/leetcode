class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
   
        ns, nt = len(s), len(t)
        
        if ns > nt:
            return self.isOneEditDistance(t,s)
        
        if nt - ns > 1:
            return False
        
      
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    ## Delete 1 char from s to make it equal to t
                    return s[i + 1:] == t[i + 1:]
                else:
                    ## Insert 1 char in s to make it equal to t
                    return s[i:] == t[i+1:]  
            
        
        ## some char after s but present in t like ab and abc
        ##print('here')
        return ns + 1 == nt
            