class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_array = []
        nums.sort() 
        print(nums)
        for i in range(len(nums)):
            target = -1 * nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    if [nums[i], nums[left], nums[right]] not in answer_array:
                        answer_array.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif current_sum > target:
                    right -=1
                else:
                    left +=1
        return (answer_array)

