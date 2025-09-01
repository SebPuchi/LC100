# Linear soltuion:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) -1
        j = 0

        while i >=0 and j < len(matrix[0]):
            print(matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j+=1
            else:
                i-=1
        return False
        



# Binary Search Solution
class Solution:
    def binarySearch(self, arr, row, target):
        left = 0
        right = len(arr[row]) -1
        while left <=right:
            mid = left + ((right - left) // 2)
            if arr[row][mid] == target:
                return True
            elif arr[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.binarySearch(matrix, i, target):
                return True
        return False
        
