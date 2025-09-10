class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        first_row_zero = False 
        first_col_zero = False 
        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    if i == 0 and j == 0:
                        first_col_zero = True
                        first_row_zero = True
                    elif i == 0:
                        first_row_zero = True
                    elif j == 0:
                        first_col_zero = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
                if matrix[i][0] == 0:
                    matrix[i][j] = 0

        print(first_row_zero, first_col_zero)
        for i in range(n):
            for j in range(m):
                if i == 0 and first_row_zero:
                    matrix[i][j] = 0
                if j == 0 and first_col_zero:
                    matrix[i][j] = 0
