class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count, oranges = 0, 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        while q and oranges > 0:
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            l = len(q)
            for i in range(l):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        print("h",row,col)
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    oranges -= 1
            count += 1
            print(count, oranges)
        return count if oranges == 0 else -1