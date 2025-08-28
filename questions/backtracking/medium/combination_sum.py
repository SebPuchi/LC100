class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_path, total):
            if total > target or start >= len(nums):
                return 
            if total == target:
                result.append(current_path.copy())
                return
            
            current_path.append(nums[start])
            backtrack(start, current_path, total + nums[start])
            current_path.pop() 
            backtrack(start +1, current_path, total)

        backtrack(0, [], 0)
        return result
