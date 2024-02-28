class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        rp = 0
        wp = len(s) - 1
        while rp <= wp:
            s[rp], s[wp] = s[wp], s[rp]
            rp += 1
            wp -= 1
        wp = 0
        
        for i in range(len(s)):
            if s[i] == " ":
                temp = i - 1
                while temp >= wp:
                    s[temp], s[wp] = s[wp], s[temp]
                    temp -= 1
                    wp += 1
                wp = i + 1
        rp = len(s) - 1
        while wp <= rp:
            s[wp], s[rp] = s[rp], s[wp]
            wp += 1
            rp -= 1
                
       
        