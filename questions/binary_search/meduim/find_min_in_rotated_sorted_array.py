class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        current_smallest = nums[0]

        while left <= right:
            mid_index = left + ((right - left) // 2)
            if nums[mid_index] < current_smallest:
                current_smallest = nums[mid_index]
                right = mid_index - 1
            else:
                left = mid_index + 1
        
        return(current_smallest)

