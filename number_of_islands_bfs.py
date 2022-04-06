from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if (grid == None or len(grid) == 0):
            return 0
            
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c]  = "0"
                    neighbors = deque()
                    neighbors.append(r * nc + c)
                    while (len(neighbors)):
                        id = neighbors.pop()
                        row, col = divmod(id, nc)
                        if row - 1 >= 0 and grid[row-1][col] == "1":
                            neighbors.append((row - 1) * nc + col)
                            grid[row - 1][col] = 0
                        if row + 1 < nr and grid[row+1][col] == "1":
                            neighbors.append((row+1) * nc + col)
                            grid[row+1][col] = "0"
                        if col -1 >= 0 and grid[row][col-1] == "1":
                            neighbors.append(row * nc + col-1)
                            grid[row][col-1] = "0"
                        if col + 1 < nc and grid[row][col+1]=="1":
                            neighbors.append(row * nc + col+1)
                            grid[row][col+1] = "0"
        
        return num_islands