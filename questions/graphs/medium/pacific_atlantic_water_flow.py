class Solution:
    def createOceanGrid(self, heights):
        oceanGrid = []
        for i in range(len(heights) +2):
            row = []
            for j in range(len(heights[0])+2):
                if i==0 and 0 <= j<= len(heights[0]) or j ==0 and i <= len(heights):
                    row.append("P")
                elif 1 <= i <= len(heights) and 1 <= j <= len(heights[0]):
                    row.append(heights[i-1][j-1])
                else:
                    row.append("A")

            oceanGrid.append(row)
        return oceanGrid
    
    def getNeighbors(self, current, grid):
        i, j = current

        neighbors = []
        if grid[i-1][j] == "P" or grid[i-1][j] == "A":
            neighbors.append(grid[i-1][j])
        elif grid[i - 1][j] <= grid[i][j]:
            neighbors.append((i-1, j))

        if grid[i+1][j] == "P" or grid[i+1][j] == "A":
            neighbors.append(grid[i+1][j])
        elif grid[i + 1][j] <= grid[i][j]:
            neighbors.append((i+1, j))

        if grid[i][j-1] == "P" or grid[i][j-1] == "A":
            neighbors.append(grid[i][j-1])
        elif grid[i][j-1] != "P" and grid[i][j-1] != "A" and grid[i][j-1] <= grid[i][j]:
            neighbors.append((i, j-1))

        if grid[i][j+1] == "P" or grid[i][j+1] == "A":
            neighbors.append(grid[i][j+1])
        elif grid[i][j+1] != "P" and grid[i][j+1] != "A" and grid[i][j+1] <= grid[i][j]:
            neighbors.append((i, j+1))

        return(neighbors)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = self.createOceanGrid(heights)

        valid_start = []

        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                visited =[]
                global_current = (i,j)
                status = []
                stack = []

                stack.append(global_current)
                while len(stack) != 0:
                    current = stack.pop() 
                    visited.append(current)
                    neighbors = self.getNeighbors(current, grid)
                    for neighbor in neighbors:
                        if neighbor == "P" or neighbor == "A":
                            status.append(neighbor)
                        elif neighbor not in visited:
                            stack.append(neighbor)
                if "P" in status and "A" in status:
                    i, j = global_current
                    valid_start.append([i-1,j-1])
                print(valid_start) 
        return valid_start




        
