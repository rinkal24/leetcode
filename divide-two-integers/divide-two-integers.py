class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        numOfNeg = 2
        if dividend >= 0:
            numOfNeg -= 1
            dividend = -dividend
        if divisor >= 0:
            numOfNeg -= 1
            divisor = -divisor
            
        doubles_List = []
        powerOfTwo_List = []
        powerOfTwo = 1
        quotient = 0
        
        while divisor >= dividend:
            doubles_List.append(divisor)
            powerOfTwo_List.append(powerOfTwo)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            powerOfTwo += powerOfTwo
            
        
        for i in reversed(range(len(doubles_List))):
            if doubles_List[i] >= dividend:
                quotient += powerOfTwo_List[i]
                dividend -= doubles_List[i]
            
        return quotient if numOfNeg != 1 else -quotient
            
        