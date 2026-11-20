class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        arr = [[0 for _ in range(c)]for _ in range(r)]
        print(obstacleGrid)
        for i in range(r):
            for j in range(c):
                print(i,j)
                if i == 0 and j == 0:
                    arr[i][j] = 1 if obstacleGrid[i][j] != 1 else 0
                elif i == 0:
                    arr[i][j] = arr[i][j - 1] if obstacleGrid[i][j] != 1 else 0
                elif j == 0: 
                    arr[i][j] = arr[i - 1][j] if obstacleGrid[i][j] != 1 else 0
                else:
                    arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) if obstacleGrid[i][j] != 1 else 0
        
        return arr[r-1][c-1]