class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # key is diff : val is index
        diffs =  {}
        current_diff = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_diff +=1
            else:
                current_diff -=1
            
            if current_diff == 0:
                longest = max(longest, i+1)
            elif current_diff in diffs:
                longest = max(longest, i - diffs[current_diff])
            
            if current_diff not in diffs:
                diffs[current_diff] = i
        return longest
