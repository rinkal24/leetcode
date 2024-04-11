class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        
        for n in nums:
            points[n] += n
            
        
        ele = sorted(points.keys())
        twoBack = 0
        oneBack = points[ele[0]]
        
        for i in range(1, len(ele)):
            if ele[i] - ele[i - 1] == 1:
                twoBack, oneBack = oneBack, max(oneBack, twoBack + points[ele[i]])
            else:
                twoBack, oneBack = oneBack, oneBack + points[ele[i]]
                 
        
        return oneBack