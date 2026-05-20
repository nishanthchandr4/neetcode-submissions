class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] <= heights[right]:
                left += 1
                area = min(heights[left], heights[right]) * (right - left)
                maxArea = max(area, maxArea)
            else: 
                right -= 1
                area = min(heights[left], heights[right]) * (right - left)
                maxArea = max(area, maxArea)
        return maxArea



