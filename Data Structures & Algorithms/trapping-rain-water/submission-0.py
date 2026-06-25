class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        ans = 0
        left = height[l]
        right = height[r]
        while l < r:
            if left < right:
                l += 1
                left = max(left,height[l])
                ans += left - height[l]
            else:
                r -= 1
                right = max(right,height[r])
                ans += right - height[r]
        return ans