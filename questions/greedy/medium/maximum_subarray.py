import math
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) 
        current_sum = sum(nums[left : right])
        while left != right:
            left=+1
            if sum(nums[left : right]) >= current_sum:
                current_sum = sum(nums[left : right])
            right-=1
            if sum(nums[left : right-1]) >= current_sum:
                current_sum = sum(nums[left : right-1])
            print(current_sum)
