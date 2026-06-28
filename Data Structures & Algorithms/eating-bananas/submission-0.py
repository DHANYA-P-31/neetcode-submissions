class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (high + low)//2
            hour = 0
            for i in piles:
                hour += (i+mid-1) // mid
            if hour <= h:
                ans = mid
                high = mid - 1
            elif hour > h:
                low = mid + 1
        return ans