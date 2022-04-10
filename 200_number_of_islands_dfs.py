class Solution:
    def dfs(self, grid: list[list[str]], r: int, c: int):
        if (r < 0) or (c < 0) or (r >= len(grid)) or (c >= len(grid[0])) or (grid[r][c] == "0"):
            return
        
        grid[r][c] = "0"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
    
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands