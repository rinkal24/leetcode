from heapq import heappush, heappop

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
      
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        maxProfit = 0
        
        heap = []
        
        for start, end, profit in jobs:
            while heap and heap[0][0] <= start:
                maxProfit = max(maxProfit, heappop(heap)[1])
            heappush(heap, (end, profit + maxProfit ))
        while heap:
            maxProfit = max(maxProfit, heappop(heap)[1])
        
        return maxProfit