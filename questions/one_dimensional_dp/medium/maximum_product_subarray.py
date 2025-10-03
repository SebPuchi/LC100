class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1
        max_prod = 1
        result = nums[0]

        for i in range(len(nums)):
            min_temp = min_prod
            min_prod = min(nums[i] * min_prod, nums[i] * max_prod, nums[i])
            max_prod = max(nums[i] * min_temp, nums[i] * max_prod, nums[i])
            result = max(result, min_prod, max_prod)

        return result
