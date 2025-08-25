class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1 
        
        while left <= right:
            mid = left + ((right - left) // 2)
            print("CURRETN", nums[mid])
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
                    right = len(nums) -1 
                    break
            elif target > nums[mid]:
                if target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
                    left = 0
                    break

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
