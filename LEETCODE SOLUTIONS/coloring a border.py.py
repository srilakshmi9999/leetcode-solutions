Coloring A Border.py


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        self.floodFill(grid, r0, c0, grid[r0][c0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    grid[i][j] = color
        return grid
        
    def floodFill(self, grid: List[List[int]], r: int, c: int, color: int):
        m, n = len(grid), len(grid[0])
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != color:
            return
        grid[r][c] = -color

        self.floodFill(grid, r, c - 1, color)
        self.floodFill(grid, r, c + 1, color)
        self.floodFill(grid, r - 1, c, color)
        self.floodFill(grid, r + 1, c, color)

        if 0 < r < m - 1 and 0 < c < n - 1:
            if abs(grid[r][c - 1]) == color and abs(grid[r][c + 1]) == color and abs(grid[r - 1][c]) == color and abs(grid[r + 1][c]) == color:
                grid[r][c] = color
