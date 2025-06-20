class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map:
                del hash_map[nums[i]]
            else:
                hash_map[nums[i]] = i
            
        return list(hash_map.keys())[0
