class Solution:
    def intToRoman(self, num: int) -> str:
        
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        i = 0
        while i < len(val) and num > 0:
            while val[i] <= num:
                num -= val[i]
                res += sym[i]
            i += 1
        return res
            