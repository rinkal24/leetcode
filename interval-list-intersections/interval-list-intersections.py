class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_ptr, s_ptr = 0, 0
        res = []
        
        while f_ptr < len(firstList) and s_ptr < len(secondList):
            f_start, f_end = firstList[f_ptr][0], firstList[f_ptr][1]
            s_start, s_end = secondList[s_ptr][0], secondList[s_ptr][1]
            
            lo = max(f_start, s_start)
            hi = min(f_end, s_end)
            
            if lo <= hi:
                res.append([lo, hi])
            if f_end < s_end:
                f_ptr += 1
            else:
                s_ptr += 1
                
                
        return res