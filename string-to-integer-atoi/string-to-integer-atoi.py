class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        pos = 0
        
        n = len(s)
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        while pos < n and s[pos] == ' ':
            pos += 1
            
        if pos < n and s[pos] == '+':
            sign = 1
            pos += 1
            
        elif pos < n and s[pos] == '-':
            sign = -1
            pos += 1
        
        while pos < n and s[pos].isnumeric():
            digit = int(s[pos])
            
            if ((res > INT_MAX // 10) or (res == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN
            
            res = 10 * res + digit
            pos += 1
            
        return res * sign
           