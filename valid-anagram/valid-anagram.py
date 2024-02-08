class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ptr1 = 0
        ptr2 = 0
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        
        while(ptr1 < len(s)):
            if s[ptr1] in d1.keys():
                d1[s[ptr1]] += 1
            else:
                d1[s[ptr1]] = 1
            ptr1 += 1
            
        while(ptr2 < len(t)):
            if t[ptr2] in d2.keys():
                d2[t[ptr2]] += 1
            else:
                d2[t[ptr2]] = 1
            ptr2 += 1
            
        
        return d1 == d2