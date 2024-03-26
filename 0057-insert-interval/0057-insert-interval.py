class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        ptr = 0
        
        while ptr < len(intervals) and intervals[ptr][1] < newInterval[0]:
            res.append(intervals[ptr])
            ptr += 1 
        
        while ptr < len(intervals) and newInterval[1] >= intervals[ptr][0]:
            newInterval[0] = min(newInterval[0], intervals[ptr][0])
            newInterval[1] = max(newInterval[1], intervals[ptr][1])
            ptr += 1
            
        res.append(newInterval)
       
        while ptr < len(intervals):
            res.append(intervals[ptr])
            ptr += 1
            
        return res