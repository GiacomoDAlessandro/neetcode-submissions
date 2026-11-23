class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        arr = [[0 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    arr[i][j] = grid[i][j]
                elif i == 0:
                    arr[i][j] = arr[i][j - 1] + grid[i][j]
                elif j == 0:
                    arr[i][j] = arr[i - 1][j] + grid[i][j]
                else:
                    arr[i][j] = min(arr[i - 1][j] + grid[i][j], arr[i][j - 1] + grid[i][j])     
        
        return arr[len(grid) - 1][len(grid[0]) - 1]