class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        max_vol = 0
        r = len(heights) - 1
        while l < r:
            min_height = min(heights[l],heights[r])
            max_vol = max(max_vol,min_height*(r-l))
            if min_height == heights[l]:
                l += 1
            else:
                r -= 1
        return max_vol