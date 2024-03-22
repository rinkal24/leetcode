class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr_m = Counter(magazine)
        ctr_r = Counter(ransomNote)
        
        for char, count in ctr_r.items():
            magazine_count = ctr_m[char]
            if magazine_count < count:
                return False
        return True