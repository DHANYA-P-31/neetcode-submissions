class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre =[1]
        suf_rev = [1]
        n = len(nums)
        for i in range(1,n):
            pre.append(pre[-1]*nums[i-1])
            suf_rev.append(suf_rev[-1]*nums[n-i])

        ans = []

        for i in range(n):
            ans.append(pre[i]*suf_rev[n-i-1])

        return ans
