class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 0:
            return True
        right = len(nums)-1
        left = right - 1
        dist_between = 1
        while left >= 0:
            if nums[left] >= dist_between:
                right = left
                left = right - 1
                dist_between = 1
            else:
                left -=1
                dist_between+=1
            
        return right == 0

