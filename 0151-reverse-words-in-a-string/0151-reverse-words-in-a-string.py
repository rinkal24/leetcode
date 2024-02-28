class Solution:
    def reverseWords(self, s: str) -> str:
        ansList = []
        ans = ""
        for i in s:
            if i != ' ':
                ans += i
            else:
                if len(ans) > 0:
                    ansList.append(ans)
                ans = ""
                continue
        if len(ans) > 0:
            ansList.append(ans)
            
        total_words = len(ansList) - 1
        res = ""
        
        while total_words >= 0:
            res += ansList[total_words] + " "
            total_words -= 1
            
        return res[:-1]