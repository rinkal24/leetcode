import collections
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        d = collections.defaultdict(list)
        nr = 0
        patternDown = True
        
        for i in range(len(s)):
            d[nr].append(s[i])
            
            if nr == numRows - 1:
                patternDown = False
                nr -= 1 if (nr - 1 >= 0) else nr

            elif nr == 0:
                patternDown = True
                nr = 1
            
            else:
                if patternDown:
                    nr += 1
                else:
                    nr -= 1
           
        res = ""
        i = 0
        
        while i < numRows and i < len(s):
            res += ''.join(d[i])
            i += 1
            
        return res