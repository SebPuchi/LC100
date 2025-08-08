class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {0:1, 1:nums[0]}
        suffix = {}

        for i in range(2, len(nums)):
                prefix[i] = nums[i-1] * prefix[i-1]

        print(prefix)
        suffix = {len(nums)-1:1, len(nums)-2:nums[len(nums)-1]}

        for i in range(len(nums)-3, -1, -1):
                suffix[i] = nums[i+1] * suffix[i+1]
        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        return(answer)
