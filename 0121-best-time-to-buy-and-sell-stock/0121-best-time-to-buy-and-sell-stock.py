class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestDifference = 0
        minSoFar = sys.maxsize
        for price in prices:
            if price < minSoFar:
                minSoFar = price
            largestDifference = max(largestDifference, price - minSoFar)
        return largestDifference