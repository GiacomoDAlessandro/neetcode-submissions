class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxA = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(row, col) -> int:
            if row < 0 or col < 0 or col >= cols or row >= rows or grid[row][col] == 0:
                return 0
            else:
                grid[row][col] = 0
                visit.add((row, col))
                return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:

                    maxA = max(maxA, dfs(i, j))
                    
        return maxA