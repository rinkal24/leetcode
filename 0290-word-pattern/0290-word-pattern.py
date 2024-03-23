class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        ctr = 0
        li = s.split(' ')
        if len(li) != len(pattern):
            return False
        for word in li:
            if word in d.values():
                key_name = list(d.keys())[list(d.values()).index(word)]
                if key_name != pattern[ctr]:
                    return False
            if pattern[ctr] not in d and word not in d.values():
                d[pattern[ctr]] = word
            
            else:
                if d[pattern[ctr]] != word:
                    return False
            ctr += 1
        return True
        