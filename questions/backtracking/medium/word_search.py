class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def dfs(i, j, index):
            if index == len(word):
                return True

            if (i < 0 or j < 0 or j >= m or i >= n or board[i][j] != word[index] or (i,j) in path):
                return False

            path.add((i, j))
            res = (dfs(i + 1, j, index + 1) or
                   dfs(i - 1, j, index + 1) or
                   dfs(i, j + 1, index + 1) or
                   dfs(i, j - 1, index + 1))
            path.remove((i, j))
            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
