class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ctr_p = Counter(p)
        start = 0
        res = []
        
        for i in range(len(s)):
            ctr_s = Counter(s[start:i + 1])
            
            if s[i] not in ctr_p:
                start = i + 1
                ctr_s = {}
                continue
                
            elif ctr_s == ctr_p:
                res.append(start)
                ctr_s[start] -= 1
                start += 1
                
                
            elif ctr_s[s[i]] > ctr_p[s[i]]:
                while start <= i:
                    ctr_s = Counter(s[start:i + 1])
                    ctr_s[s[start]] -= 1
                    if ctr_s[start] == 0:
                        del ctr_s[start]
                    start += 1
                    if s[start - 1] == s[i]:
                        break      
                    
        return res
                