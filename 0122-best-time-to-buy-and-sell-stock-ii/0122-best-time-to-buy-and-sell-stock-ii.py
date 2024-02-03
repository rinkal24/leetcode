class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        valley = sys.maxsize
        peak = valley
        
        for i in range(len(prices)):
            if prices[i] < peak:
                total += peak - valley
                
                valley = prices[i]
                peak = valley
                
            else:
                peak = prices[i]
        total += peak - valley
        return total
        