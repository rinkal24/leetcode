class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        
        for n in nums:
            points[n] += n
            max_num = max(max_num, n)
            
        
        n = len(points)
        twoBack = oneBack = 0
        
        if max_num < n + n*log(n,2):
            oneBack = points[1]
            for num in range(2, max_num + 1):
                twoBack, oneBack = oneBack, max(oneBack, twoBack + points[num])
        else:
            ele = sorted(points.keys())
            oneBack = points[ele[0]]
            for i in range(1, len(ele)):
                if ele[i] - ele[i - 1] == 1:
                    twoBack, oneBack = oneBack, max(oneBack, twoBack + points[ele[i]])
                else:
                    twoBack, oneBack = oneBack, oneBack + points[ele[i]]
                 
        
        return oneBack