class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def getNeighbors(node):
            i, j = node
            n_out = []
            if i-1 >= 0 and grid[i-1][j] == 1:
                n_out.append((i-1, j))
            if j-1 >= 0 and grid[i][j-1] == 1:
                n_out.append((i, j-1))
            if i + 1 < n and grid[i+1][j] == 1:
                n_out.append((i+1, j))
            if j + 1 < m and grid[i][j+1] == 1: 
                n_out.append((i, j+1))
            return n_out

        time = 0
        fresh_oranges = 0
        queue = []
        fresh_visited = 0
        visited = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges +=1
                if grid[i][j] == 2:
                    queue.append((i,j))

        while len(queue) != 0:
            # pop all rotten oranges:
            for i in range(len(queue)):
                node = queue.pop(0)
                visited.append(node)
                neighbors = getNeighbors(node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        x, y = neighbor
                        grid[x][y] = 2
                        queue.append(neighbor)
                        fresh_visited +=1
            time+=1
        if fresh_oranges == 0:
            return 0
        elif fresh_visited == fresh_oranges:
            return time -1
        else:
            return -1

