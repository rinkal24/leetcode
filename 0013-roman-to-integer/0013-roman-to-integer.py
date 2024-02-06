class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"X":10, "V":5, "I":1, "L":50, "C":100 , "D": 500, "M":1000}
        total = 0
        prev = s[0]
        for i in s:
            if (i in ["V", "X"] and prev == "I") or (i in ["L", "C"] and prev == "X") or (i in ["D", "M"] and prev == "C"):
                total += d[i] - 2* d[prev]
                print(total)
            else:
                total += d[i]
                print("else total", total)
            prev = i
            print("prev", prev)
            
        return total