class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, 0

        while True:
            next_index = nums[left]
            next_next_index = nums[nums[right]]

            left = next_index
            right = next_next_index
            if nums[left] == nums[right]:
                break
        right_two = 0

        while True:
            if nums[left] == nums[right_two]:
                return nums[left]
            
            left = nums[left]
            right_two = nums[right_two]
