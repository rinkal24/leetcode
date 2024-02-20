# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n 
        minVal = hi
        
        while lo < hi:
            mid = int((lo + hi )/2)
            if isBadVersion(mid):
                minVal = min(minVal, mid)
                hi = mid
            else:
                lo = mid + 1
        return minVal
        
            