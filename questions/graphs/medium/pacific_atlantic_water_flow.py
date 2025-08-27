class Solution:
    def getAtlantic (self, node, heights):
        n = len(heights)
        m = len(heights[0])
        i = node[0]
        j = node[1]

        neighbors = []
        if i-1 >= 0 and heights[i-1][j] >= heights[i][j]:
            neighbors.append([i-1, j])

        if i+1 < n and heights[i+1][j] >= heights[i][j]:
            neighbors.append([i+1, j])

        if j - 1 >= 0 and heights[i][j-1] >= heights[i][j]:
            neighbors.append([i, j-1])

        if j+1 < m and heights[i][j+1] >= heights[i][j]:
            neighbors.append([i, j+1])
        return neighbors
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        valid = []
        reach_pacific = []
        reach_atlantic = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i == 0 and 0 <= j < len(heights[0])) or (j == 0 and 0 <=i < len(heights)):
                    current = [i,j]
                    if current not in reach_pacific:
                        stack = []
                        stack.append(current)
                        while len(stack) != 0:
                            node = stack.pop()
                            reach_pacific.append(node)
                            neighbors = self.getAtlantic(node, heights)
                            for neighbor in neighbors:
                                if neighbor not in reach_pacific:
                                    stack.append(neighbor)
                if (j == len(heights[0])-1 and 0 <= i < len(heights)) or (i == len(heights)-1 and 0 <= j < len(heights[0])):
                    current = [i,j]
                    if current not in reach_atlantic:
                        stack = []
                        stack.append(current)
                        while len(stack) != 0:
                            node = stack.pop()
                            reach_atlantic.append(node)
                            neighbors = self.getAtlantic(node, heights)
                            for neighbor in neighbors:
                                if neighbor not in reach_atlantic:
                                    stack.append(neighbor)
                    
        output = []
        print(reach_pacific)
        print(reach_atlantic)
        for i in range(len(reach_atlantic)):
            if reach_atlantic[i] in reach_pacific and reach_atlantic[i] not in output:
                output.append(reach_atlantic[i])
        return(output)
 


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




        
