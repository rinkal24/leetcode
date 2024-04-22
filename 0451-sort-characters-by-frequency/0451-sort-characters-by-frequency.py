class Solution:
    def frequencySort(self, s: str) -> str:
        ctr_s = Counter(s)
        max_freq = max(ctr_s.values())
        
        
        buckets = [[] for _ in range(max_freq + 1)]
        
        
        res = ""
        
        for letter,freq in ctr_s.items():
            buckets[freq].append(letter)
            
        
        for i in reversed(range(len(buckets))):
            for j in buckets[i]:
                res += j * i
        
        
            
        
        return res
        