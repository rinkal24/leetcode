class Solution:
    
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' :
            return 0
        
        one_back = 1
        two_back = 1
        
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr = one_back
            
            two_digit = int(s[i - 1:i + 1])
            if two_digit >= 10 and two_digit <= 26:
                curr += two_back
            two_back = one_back
            one_back = curr
            
        return one_back