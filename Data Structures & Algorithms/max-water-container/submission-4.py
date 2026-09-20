class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0 
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if area > max:
                max = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max