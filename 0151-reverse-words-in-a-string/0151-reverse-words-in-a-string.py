class Solution:
    def reverseWords(self, s: str) -> str:
        ansList = []
        ans = ""
        res = ""
        for i in s:
            if i != ' ':
                ans += i
            else:
                if len(ans) > 0:
                    ansList.append(ans)
                    res = " "+ ans + res
                ans = ""
                continue
        
        if len(ans) > 0:
            ansList.append(ans)
            res = ans + res + " "
        total_words = len(ansList) - 1
        print(res)
        """
        res = ""
        
        while total_words >= 0:
            res += ansList[total_words] + " "
            total_words -= 1
        """
        return res.strip()