class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        res = ""
        for i in s:
            if i != ' ':
                ans += i
            else:
                if len(ans) > 0:
                    res = " "+ ans + res
                ans = ""
                continue
        
        if len(ans) > 0:
            res = ans + res + " "
        
        return res.strip()