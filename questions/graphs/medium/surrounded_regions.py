class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        traverse_nodes = []

        def getNeighbors(node):
            i, j = node
            neighbors = []
            if i - 1 >=0 and board[i-1][j] == 'O':
                neighbors.append((i-1,j))

            if i +1 < n and board[i+1][j] == 'O':
                neighbors.append((i+1,j))

            if j - 1 >=0 and board[i][j-1] == 'O':
                neighbors.append((i,j-1))

            if j + 1 < m and board[i][j+1] == 'O':
                neighbors.append((i,j+1))

            return neighbors

        def explore(current):
            visited = set()
            stack = []
            stack.append(current)

            while len(stack) != 0:
                val = stack.pop(0)
                i, j = val
                board[i][j] = '#'

                neighbors = getNeighbors(val)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

        # main exec 
        for i in range(n):
            for j in range(m):
                if i == 0 and 0<= j < m or (i == n-1 and 0<=j<m):
                    if board[i][j] == 'O':
                        traverse_nodes.append((i,j))

                if j == 0 and 0<= i < n or (j == m-1 and 0<=i<n):
                    if board[i][j] == 'O':
                        traverse_nodes.append((i,j))

        for node in traverse_nodes:
            for i in range(n):
                print(board[i])
            print()
            explore(node)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
