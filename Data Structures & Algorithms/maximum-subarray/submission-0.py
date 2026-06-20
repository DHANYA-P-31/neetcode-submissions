class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if m+nums[i] > nums[i]:
                m = m+nums[i]
            else:
                m = nums[i]
            ans = max(ans,m)
        return ans

        