class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_to_last = len(nums) - 1
        last_jump = nums[0]
        i = 0
        while i < len(nums):
            if i < 0:
                break
            if nums[i] == 0:
                if i == len(nums) - 1:
                    return True
                else: 
                    i -= last_jump
                    nums[i] = nums[i] - 1
                    len_to_last+=last_jump
                    continue

            if nums[i] >= len_to_last:
                return True
            else:
                last_jump = nums[i]
                i += last_jump
                len_to_last -= last_jump
        return False

