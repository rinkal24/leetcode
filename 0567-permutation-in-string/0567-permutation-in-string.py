from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr_s1 = Counter(s1)
        ctr_s2 = defaultdict()
        start = 0
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s2)):
            ctr_s2 = Counter(s2[start: i + 1])
            if s2[i] not in ctr_s1:
                start = i + 1
                ctr_s2 = {}
                continue
            
            elif ctr_s2 == ctr_s1:
                return True
            
            elif ctr_s2[s2[i]] > ctr_s1[s2[i]]:
                while start <= i:
                    ctr_s2 = Counter(s2[start:i + 1])
                    ctr_s2[s2[start]] -= 1
                    if ctr_s2[start] == 0:
                        del ctr_s2[start]
                    start += 1
                    if s2[start - 1] == s2[i]:
                        break 
           
        return False
                