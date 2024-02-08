class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        start_ind = 0
        end_ind = 1
        maxlen = 1
        temp = 1
        d = {str(s[0]):0}      
        
        while(start_ind <= end_ind and end_ind < len(s)):
            print("start=",s[start_ind],start_ind,"end",s[end_ind], end_ind)
            if s[end_ind] in d.keys() and d[s[end_ind]] >= start_ind:
                start_ind = d[s[end_ind]] + 1
                d[s[end_ind]] = end_ind
                end_ind += 1
                maxlen = max(maxlen, end_ind - start_ind)
                temp = 1
                
            else:
                d[s[end_ind]] = end_ind
                end_ind += 1
                
                
            maxlen = max(maxlen, end_ind - start_ind )
        return maxlen
                
                
                