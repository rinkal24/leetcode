class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        d = {}
        nr = 0
        patternDown = True
        
        for i in range(len(s)):
            if nr not in d:
                d[nr] = [s[i]]
            else:
                d[nr] += s[i]
                
            if i + 1 == len(s):
                break
            
            elif nr == numRows - 1:
                patternDown = False
                if nr - 1 >= 0:
                    nr -= 1
                continue

            elif nr == 0:
                patternDown = True
                nr = 1
                continue

            # (nr + 1 < numRows) and (nr > 0):
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