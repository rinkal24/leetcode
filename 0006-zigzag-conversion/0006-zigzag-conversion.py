class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = [['' for _ in range(len(s))] for _ in range(numRows)]
        
        nr = 0
        nc = 0
        patternDown = True
        
        for i in range(len(s)):
            d[nr][nc] = s[i]
            
            if i + 1 == len(s):
                break
            
            elif nr == numRows - 1:
                patternDown = False
                nc += 1
                if nr - 1 >= 0:
                    nr -= 1
                continue

            elif nr == 0:
                patternDown = True
                nr += 1
                continue

            # (nr + 1 < numRows) and (nr > 0):
            if patternDown:
                nr += 1
            else:
                nr -= 1
                nc += 1
                    
    
        index = 0
        res = ""
        
        
        for i in range(numRows):
            for j in range(nc + 1):
                if d[i][j] != '':
                    res += d[i][j]
            
        
        return res