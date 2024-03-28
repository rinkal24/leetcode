class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        res = []
        
        while (num != 1 and num not in res ) :
            val = num
            num = str(num)
            total = 0
            for n in num:
                total += int(n)*int(n)
            num = int(total)
            res.append(val)
        return True if num == 1 else False