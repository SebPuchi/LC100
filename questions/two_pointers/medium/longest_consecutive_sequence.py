class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort() 
        print(nums)
        left = 0
        right = 1
        max_count = 1
        count = 1
        while left < len(nums)-1:
            if nums[left] == nums[right]:
                right +=1
                left +=1
                continue
            elif nums[left] == nums[right] -1:
                count+=1
                right+=1
                left+=1
                if count > max_count:
                    max_count = count
            else:
                left = right
                right = right + 1
                count = 1

        return max_count
