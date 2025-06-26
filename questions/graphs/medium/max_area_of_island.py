class Solution:
    def getNeighbors(self, grid, current):
        max_x = len(grid)
        max_y = len(grid[0])
        neighbors = []
        x, y = current

        if x + 1 < max_x:
           if grid[x+1][y] == 1:
            neighbors.append((x+1,y))

        if x - 1 >= 0:
           if grid[x-1][y] == 1:
            neighbors.append((x-1,y))
         
        if y + 1 < max_y:
           if grid[x][y+1] == 1:
            neighbors.append((x,y+1))

        if y - 1 >= 0:
           if grid[x][y-1] == 1:
            neighbors.append((x,y-1))
        return neighbors


    def explore(self, grid, current, visited):
        visited.append(current)
        neighbors = self.getNeighbors(grid, current)
        area = 1

        for neighbor in neighbors:
            if neighbor not in visited:
                area += self.explore(grid, neighbor, visited)
        return area 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        current_max = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                current = (i,j)

                if grid[i][j] == 0:
                    continue
                
                if current not in visited: 
                    visited.append(current)
                    area = self.explore(grid, current, visited)
                    print(area)
                    if area > current_max:
                        current_max = area
        return current_ma
