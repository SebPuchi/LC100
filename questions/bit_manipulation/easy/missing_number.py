class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            total_sum += (i - nums[i])

        # Add final value in n array which in len(n)
        return total_sum + len(nums)
