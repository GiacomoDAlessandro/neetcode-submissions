class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)]for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    arr[i][j] = 1
                elif i == 0:
                    arr[i][j] = arr[i][j - 1]
                elif j == 0:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

        return arr[m - 1][n - 1]