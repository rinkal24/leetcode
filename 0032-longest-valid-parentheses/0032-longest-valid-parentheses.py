class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        ctr = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                ctr = max(ctr, 2* right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for i in range(n - 1, 0, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                ctr = max(ctr, 2 * left)
            elif left > right:
                left = right = 0
        return ctr