class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        left = 0
        right = len(nums) -1
        while right >= left:
            mid_index = left + ((right - left) // 2)
            if target == nums[mid_index]:
                index = mid_index
                break
            elif target > nums[mid_index]:
               left = mid_index +1 
            else:
                right = mid_index -1
        return index
