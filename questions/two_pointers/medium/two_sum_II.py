class Solution(object):

# SOLUTION WITH BINARY SEARCH
    def binarySearch(self, target, nums, left, right):
        while left <= right:
            print(left, right)
            mid_index = left + ((right-left) // 2)
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                right = mid_index - 1
            else: 
                left = mid_index +1
        return None 

    def twoSum(self, numbers, target):
    
        for i in range(len(numbers)):
            search_index = self.binarySearch(target - numbers[i], numbers, i+1, len(numbers)-1)         
            if (search_index):
                return [i+1, search_index+1]


# BETTER SOLUITION: TWO POINTER
   def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left+=1
            else: 
                right-=1
        return []


