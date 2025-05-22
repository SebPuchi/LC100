class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1

        while right >= left:

            middle_index = left + ((right - left) // 2)

            if matrix[middle_index][0] == target:
                return True
            elif matrix[middle_index][0] > target:
                right = middle_index -1
            elif matrix[middle_index][0] < target and target <= matrix[middle_index][-1]:
                break
            else:
                left = middle_index +1
        
        approx_arr = matrix[middle_index]

        left = 0
        right = len(approx_arr) -1
        while right >= left:

            middle_index = left + ((right - left) // 2)

            if approx_arr[middle_index] == target:
                return True
            elif approx_arr[middle_index] > target:
                right = middle_index -1
            else: 
                left = middle_index +1

        return False
