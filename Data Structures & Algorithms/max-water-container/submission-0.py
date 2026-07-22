class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        biggest = 0
        while left < right:
            result = (abs(left - right) * min(heights[left], heights[right]))
            biggest = max(biggest, result)
            
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1
        
        return biggest