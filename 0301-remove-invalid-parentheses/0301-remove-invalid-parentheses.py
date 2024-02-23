from collections import deque

class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:

        # helper to check if the expression is valid
        def isValid(expr):
            count = 0
            for ch in expr:
                if ch not in '()':
                    continue
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if len(s) == 0:
            return [""]

        visited = set()

        Q = deque()
        Q.append(s)
        visited.add(s)

        foundFlag = False
        ans = []

        while Q:
            val = Q.popleft()

            if isValid(val):
                ans.append(val)
                foundFlag = True

            if foundFlag:
                continue

            for i in range(len(val)):
                if val[i] not in '()':
                    continue

                charVal = val[:i] + val[i+1:] 
                if charVal not in visited:
                    Q.append(charVal)
                    visited.add(charVal)
    
        return ans if ans else [""]