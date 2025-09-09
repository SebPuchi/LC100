class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        grid = matrix
        output = []
        n  = len(matrix)
        m  = len(matrix[0])

        if n ==1 and m == 1:
            return grid[0]

        # starting point:
        i, j = 0,0
        cell_count = 0
        while cell_count != (n * m):
            # move right: 
            while j != m and grid[i][j] != "#":
                output.append(grid[i][j])
                grid[i][j] = "#"
                j+=1
                cell_count+=1
            j-=1
            i+=1
            # move down: 
            while i != n and grid[i][j] != "#":
                output.append(grid[i][j])
                grid[i][j] = "#"
                i+=1
                cell_count+=1
            i-=1
            j-=1
            # move left: 
            while j >= 0 and grid[i][j] != "#":
                output.append(grid[i][j])
                grid[i][j] = "#"
                j-=1
                cell_count+=1
            j+=1
            i-=1
            # move up: 
            while i >= 0 and grid[i][j] != "#":
                output.append(grid[i][j])
                grid[i][j] = "#"
                i-=1
                cell_count+=1
            i+=1
            j+=1
        return(output)
