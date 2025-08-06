class Solution:

    def recurseTwo(self, i, nums, memo):
        if i == 1:
            memo[i] = nums[1] 
        elif i == 2:
            memo[i] = max(nums[1], nums[2])
        else:
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
 
    def recurseOne(self, i, nums, memo):
        if i == 0:
            memo[i] = nums[0] 
        elif i == 1:
            memo[i] = max(nums[0], nums[1])
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
        for i in range(len(nums)-1):
            self.recurseOne(i, nums, memo_one)
        for i in range(1, len(nums)):
            self.recurseTwo(i, nums, memo_two)
        vals_one = list(memo_one.values())
        print(vals_one)
        vals_two = list(memo_two.values())
        print(vals_two)
        return max(max(vals_one), max(vals_two))

