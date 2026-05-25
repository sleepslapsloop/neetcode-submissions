class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def area(arr: List[int], left: int, right: int) -> int:
            return min(arr[left], arr[right]) * (right - left)

        left, right = 0, len(heights) - 1
        maxArea = area(heights, left, right)

        while left < right:
            currArea = area(heights, left, right)
            maxArea = currArea if currArea > maxArea else maxArea

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea            
