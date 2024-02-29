class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = [['' for _ in range(len(s))] for _ in range(numRows)]
        
        
        nr = 0
        nc = 0
        patternDown = True
        
        for i in s:
            if nr == numRows and d[0][0] != 0:
                patternDown = False
                nr -= 2
                nc += 1
                
            d[nr][nc] = i
            
            if (nr < numRows) and (nr >= 0):
                if patternDown:
                    nr += 1
                else:
                    if nr == 0:
                        patternDown = True
                        nr += 1
                    else:
                        nr -= 1
                        nc += 1
            elif nr < 0:
                nr = 1
                patternDown = False
        
        index = 0
        res = ""
        
        
        for i in range(numRows):
            for j in range(nc + 1):
                if d[i][j] != '':
                    res += d[i][j]
            
        
        return res