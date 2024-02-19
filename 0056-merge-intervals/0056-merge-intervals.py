class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        res, prev = [], []
        i = 0
        
        intervals = sorted(intervals)
        while i < len(intervals) - 1:
            if len(prev) > 0:
                first_start, first_end = prev[0], prev[1]
            else:
                first_start, first_end = intervals[i][0], intervals[i][1]
            sec_start, sec_end = intervals[i + 1][0], intervals[i + 1][1]
            
            
            if sec_start <= first_end and sec_end >= first_start:
                if len(prev) > 0:
                    res.pop()
                res.append([min(first_start, sec_start), max(first_end, sec_end)])
                prev = [res[-1][0], res[-1][1]]
                
            else:
                if i == 0:
                    if first_start < sec_start:
                        res.append([first_start, first_end])
                        res.append([sec_start, sec_end])
                        
                    else:
                        res.append([sec_start, sec_end])
                        res.append([first_start, first_end])
                else:
                    res.append([sec_start, sec_end])
                prev = [res[-1][0], res[-1][1]]
            
            i += 1
        
        return res
                
            