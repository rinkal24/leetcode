class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr_m = Counter(magazine)
        ctr_r = Counter(ransomNote)
        
        for c in ctr_r:
            if ctr_m[c] < ctr_r[c]:
                return False
        return True