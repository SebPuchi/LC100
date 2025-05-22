class Solution:
    def search(self, nums: List[int], target: int, left = None, right = None) -> int:
        if left is None and right is None:
            left = 0
            right = len(nums) -1
        if left == right:
            if nums[left] == target:
                return left 
            else: 
                return -1
                
        mid_index = right - left // 2
        if target == nums[mid_index]:
            return mid_index
        elif target > nums[mid_index]:
            return self.search(nums, target, mid_index +1, right)
        else:
            return self.search(nums, target, left, mid_index - 1)
