class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, lo, hi):
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return checkPalindrome(s, lo, hi - 1) or checkPalindrome(s, lo + 1, hi)
            lo += 1
            hi -= 1
            
        return True