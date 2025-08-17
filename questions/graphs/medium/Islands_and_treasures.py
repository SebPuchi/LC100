class Solution:

    def getNeighbors(self, grid, current, n, m):
        neighbors = []
        i, j = current

        if i+1 < n and grid[i+1][j] != -1:
            neighbors.append((i+1,j)) 

        if i-1 >= 0 and grid[i-1][j] != -1:
            neighbors.append((i-1,j)) 

        if j+1 < m and grid[i][j+1] != -1:
            neighbors.append((i,j+1)) 

        if j-1 >= 0 and grid[i][j-1] != -1:
            neighbors.append((i,j-1)) 
        return neighbors

    def bfs(self, grid, current, visited, n, m):
        queue = []
        queue.append((current, 1))
        while queue:
            current, dist = queue.pop(0)
            visited.append(current)
            neighbors = self.getNeighbors(grid, current, n, m)
            for neighbor in neighbors:
                n_i, n_j = neighbor
                if grid[n_i][n_j] == 0:
                    return dist
                if neighbor not in visited:
                    queue.append((neighbor, dist+1))

        return None

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1 and grid[i][j] != 0:
                    print("CURRENT", grid[i][j])
                    found = self.bfs(grid, (i,j), [], n, m)
                    print("FOUND", found)
                    if found != None:
                        grid[i][j] = found
        print(grid)
