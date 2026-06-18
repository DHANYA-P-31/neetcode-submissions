class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = []
        suf = []
        ans = []
        pref= 1
        sufi = 1
        ansi = 1
        for i in range(n):
            pre.append(pref)
            suf.append(sufi)
            pref *= nums[i]
            sufi *= nums[n-1-i]
        for i in range(n):
            ansi = pre[i] * suf[n-1-i]
            ans.append(ansi)
        
        return ans