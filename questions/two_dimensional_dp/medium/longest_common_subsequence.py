class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        grid = []
        for i in range(len(text1)+1):
            row = []
            for j in range(len(text2)+1):
                row.append(0) 
            grid.append(row)
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        
        return(grid[0][0])

