class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        arr = [[0] * cols for __ in range(rows)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 or j == cols - 1:
                    arr[i][j] = 1 if matrix[i][j] == 1 else 0
                else:
                    m = min(arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])
                    if m == 0:
                        arr[i][j] = 1 if matrix[i][j] == 1 else 0
                    else:
                        arr[i][j] = (1 + m) if matrix[i][j] == 1 else 0

        return sum(sum(row)for row in arr)
