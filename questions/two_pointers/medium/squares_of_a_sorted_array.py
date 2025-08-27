class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1

        print(right)
        answer_array = [None] * len(nums)
        print(answer_array)
        count = -1
        while left <= right:
            if (nums[left])**2 > (nums[right])**2:
                answer_array[count] = nums[left]**2
                left+=1 
            else:
                answer_array[count] = nums[right]**2
                right-=1 
            count-=1
        return(answer_array)
        
