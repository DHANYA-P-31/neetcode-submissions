class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i+1,n):
                target = -(nums[i]+nums[j])
                if target in seen:
                    ans.add(tuple(sorted([nums[i],nums[j],target])))
                seen.add(nums[j])
        return [list(x) for x in ans]