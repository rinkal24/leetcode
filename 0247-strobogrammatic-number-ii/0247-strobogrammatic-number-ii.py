class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        def helper(n, target):
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                return ["11","69","88","96"]
            res = helper(n - 2, target)
            
            if n - 2 == 2:
                res.append("00")
            
            
            d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
            
            ans = []
            for i in res:
                for k in d.keys():
                    if n == target and k == "0":
                        continue
                    ans.append(k + i + d[k])
                
            return ans
        
        return helper(n, n)
            