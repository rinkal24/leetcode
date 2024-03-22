class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        for c in ransomNote:
            if c not in magazine:
                return False
            loc = magazine.index(c)
            magazine = magazine[:loc] + magazine[loc + 1:]
            
        return True