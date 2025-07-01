class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        print(m, n)
        grid = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                if j == n or i ==m:
                    row.append(0)
                else:
                    row.append(None)
            grid.append(row)
        grid[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n -1, -1, -1):
                if i == m -1 and j == n-1:
                    continue 
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]


