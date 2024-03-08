class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stk = []
        stk.append(-1)
        ctr = 0
        
        for i in range(n):
            if s[i] == "(":
                stk.append(i)
            else:
                stk.pop()
                if len(stk) == 0:
                    stk.append(i)
                else:
                    ctr = max(ctr, i - stk[-1])
        return ctr