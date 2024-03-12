class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1/helper(x, -n)
            if n % 2 == 1:
                return x * helper(x*x, (n-1)//2)
            else:
                return helper(x*x, n//2)
            return x * helper(x, n- 1)
        return helper(x, n)