class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        leftptr = 0
        while(i < len(s) and leftptr < len(t)):
            if s[i] == t[leftptr]:
                i += 1
                leftptr += 1
            else:
                leftptr += 1
        if i == len(s):
            return True
        return False