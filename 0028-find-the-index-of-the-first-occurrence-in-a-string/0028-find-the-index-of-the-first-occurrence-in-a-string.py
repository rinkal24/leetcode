class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        len_n = len(needle)
        len_h = len(haystack)
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                rp_n = 0
                rp_h = i
                while rp_n < len_n and rp_h < len_h:
                    if needle[rp_n] != haystack[rp_h]:
                        break
                    rp_h += 1
                    rp_n += 1
                    
                if rp_n == len_n:
                    return i
                
        return -1
                    