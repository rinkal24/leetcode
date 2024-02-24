class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        num_dict = {"0":"0","1":"1", "6":"9", "8":"8", "9":"6"}
        
        res = ""
        for n in num:
            res += num_dict[n] if n in num_dict else "0"
        ans = ''.join(reversed(res))
        return ans == num
            