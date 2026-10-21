class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)]for _ in range(m)]
        print(arr)
        for i in range(m):  
            for k in range(n):
                if i == 0 and k == 0:
                    arr[i][k] = 1
                elif i == 0 or k == 0:
                    arr[i][k] = 1
                else:
                    arr[i][k] = arr[i - 1][k] + arr[i][k - 1]
        return arr[m-1][n-1]