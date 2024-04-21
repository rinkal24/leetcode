class Solution:
    def frequencySort(self, s: str) -> str:
        ctr_s = Counter(s)
        
        ctr_s = sorted(ctr_s.items(), key = lambda x:x[1], reverse = True)
        
        res = ""
        
        for i in range(len(ctr_s)):
            res += ctr_s[i][0] * ctr_s[i][1]
            
        
        return res
        