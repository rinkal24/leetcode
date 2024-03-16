class Solution:
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        
        if r >= nr or r < 0 or c < 0 or c >= nc or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        numOfIslands = 0
        
        nr = len(grid)
        nc = len(grid[0])
        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numOfIslands += 1
        return numOfIslands