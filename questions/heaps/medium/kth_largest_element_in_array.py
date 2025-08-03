import heapq
class Solution:
    def sort(self, nums, k):
        int_max = nums[0]
        index = 0
        for z in range(k):
            for i in range(len(nums) - z):
                print(nums[i])
                if nums[i] > int_max:
                    int_max = nums[i]
                    index = i
            temp = nums[len(nums)-1-z]
            nums[len(nums) - 1 -z] = int_max 
            nums[index] = temp

            print(int_max, nums)
        return nums[len(nums)-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        no_dup = []
        for i in range(len(nums)):
            if nums[i] not in no_dup:
                no_dup.append(nums[i])
 
        return(self.sort(no_dup, k))

# Heap solution:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1

