class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

            
        quotient = 0
        while divisor >= dividend:
            powerOfTwo = -1
            val = divisor
            while val >= HALF_MIN_INT and val + val >= dividend:
                val +=val
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= val
            
        return -quotient if negatives != 1 else quotient