class Solution:

    def recurseTwo(self, i, nums, memo):
        if i == 2:
            memo[i] = nums[2] 
        elif i == 3:
            memo[i] = max(nums[2], nums[3])
        else:
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
 
    def recurseOne(self, i, nums, memo):
        if i == 0 or i == 1:
            memo[i] = max(nums[i-2] + nums[i], nums[i-1])
        else:
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2 or len(nums) == 3:
            return max(nums)
        else:
            memo_one = {}
            memo_two = {}
        for i in range(len(nums)-2):
            self.recurseOne(i, nums, memo_one)
        for i in range(2, len(nums)):
            self.recurseTwo(i, nums, memo_two)
        vals_one = list(memo_one.values())
        vals_two = list(memo_two.values())
        return max(max(vals_one), max(vals_two))
