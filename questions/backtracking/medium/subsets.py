class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, current_path):
            if index >= len(nums):
                result.append(current_path.copy())
                return 
            current_path.append(nums[index])
            backtrack(index+1, current_path)
            current_path.pop()
            backtrack(index+1, current_path)

        backtrack(0, [])
        return(result)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start: int, path: List[int]):
            res.append(path[:])  
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()           
        
        backtrack(0, [])
        return res
