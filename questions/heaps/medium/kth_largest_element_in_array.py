import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

       for i in range(len(nums)):
            nums[i] =nums[i] * -1
        
       print(nums)
       for i in range(len(nums)):
            val = heapq.heappop(nums) 
            print(val)
       print(nums
