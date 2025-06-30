class Solution:
    def recurse(self, i, memo, nums):
        memo[i] = max(memo[i-2] + nums[i], memo[i-1])


    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))
        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        for i in range(2, len(nums)):
            self.recurse(i, memo, nums)
        print(memo)
        return memo[len(nums)-1]
