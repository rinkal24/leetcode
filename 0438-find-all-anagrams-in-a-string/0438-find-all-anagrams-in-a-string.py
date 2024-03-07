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
                #print('here', ctr_s, start, i)
                res.append(start)
                ctr_s[start] -= 1
                start += 1
                
                
            elif ctr_s[s[i]] > ctr_p[s[i]]:
                while start <= i:
                    ctr_s = Counter(s[start:i + 1])
                    #print('inside', ctr_s, start, i)
                    if s[start] == s[i] and ctr_s[s[start]] <= ctr_p[s[start]]:
                        break
                    ctr_s[s[start]] -= 1
                    if ctr_s[start] == 0:
                        del ctr_s[start]
                    start += 1
                    
                    if s[start - 1] == s[i] and ctr_s[s[start - 1]] <= ctr_p[s[start - 1]]:
                        break
            #print(ctr_s, start, s[start], s[i])       
                    
        return res
                