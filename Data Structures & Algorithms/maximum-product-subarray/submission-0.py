class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax = 1
        cmin = 1
        ans = nums[0]
        for i in nums:
            temp = cmax*i
            cmax = max(temp,cmin*i,i)
            cmin = min(temp,cmin*i,i)
            ans = max(ans,cmax)
        return ans
        