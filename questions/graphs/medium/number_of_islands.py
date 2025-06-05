class Solution:
    def getNeighbors(self, graph, current):
        neighbors = []
        x, y = current
        rows = len(graph)
        cols = len(graph[0])

        # Check down
        if x + 1 < rows:
            neighbors.append((x + 1, y))

        # Check up
        if x - 1 >= 0:
            neighbors.append((x - 1, y))

        # Check right
        if y + 1 < cols:
            neighbors.append((x, y + 1))

        # Check left
        if y - 1 >= 0:
            neighbors.append((x, y-1))  
        return neighbors


    def explore(self, graph, current, visited_nodes):
        x, y = current
        if graph[x][y] != "0":
            visited_nodes.append(current)
            neighbors_list = self.getNeighbors(graph, current)
            for neighbor in neighbors_list:
                if neighbor not in visited_nodes: 
                    self.explore(graph, neighbor, visited_nodes)
            return 1
        else: 
            return 0

    def numIslands(self, grid: List[List[str]]) -> int:
        visited_nodes = []
         
        island_counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                current = (x,y)
                if current not in visited_nodes: 
                    island_counter += self.explore(grid, current, visited_nodes)
        print(island_counter)
        return island_counter





