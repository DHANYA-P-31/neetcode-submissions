class Solution:
    def threeSum(self, nums):
        ans = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i+1,n):
                val = - (nums[i]+nums[j])
                if val in seen:
                    ans.add(tuple(sorted((nums[i],val,nums[j]))))
                seen.add(nums[j])
        return [list(x) for x in ans]
