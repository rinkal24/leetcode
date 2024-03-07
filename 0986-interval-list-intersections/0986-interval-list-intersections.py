class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_ptr = 0
        s_ptr = 0
        res = []
        
        
        
        while f_ptr < len(firstList) and s_ptr < len(secondList):
            lo = max(firstList[f_ptr][0], secondList[s_ptr][0])
            hi = min(firstList[f_ptr][1], secondList[s_ptr][1])
            
            if lo <= hi:
                res.append([lo, hi])
            if firstList[f_ptr][1] < secondList[s_ptr][1]:
                f_ptr += 1
            else:
                s_ptr += 1
        return res