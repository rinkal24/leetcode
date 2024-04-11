class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        
        for n in nums:
            points[n] += n
            max_num = max(max_num, n)
            
        @cache
        def dfs(num):
            if num == 0:
                return 0
            if num == 1:
                return points[num]
            return max(dfs(num - 1), dfs(num - 2) + points[num])
        
        return dfs(max_num)