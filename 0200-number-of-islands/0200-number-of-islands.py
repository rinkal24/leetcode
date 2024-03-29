class Solution:
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        
        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
            return 
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        num_Islands = 0
        nr = len(grid)
        nc = len(grid[0])
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    num_Islands += 1
                    
        return num_Islands
        