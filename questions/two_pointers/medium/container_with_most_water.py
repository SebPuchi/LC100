class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = -1
        while left != right:
            if heights[left] <= heights[right]:
                max_water = max(max_water, (right-left) * heights[left])
                left +=1
            else:
                max_water = max(max_water, (right-left) * heights[right])
                right -=1
        return(max_water)
