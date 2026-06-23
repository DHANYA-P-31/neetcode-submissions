class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums):
            p1,p2 = 0,0
            for n in nums:
                p2, p1 = p1, max(p1,p2+n)
            return p1
        if len(nums) == 1:
            return nums[0]
        return max(solve(nums[1:]),solve(nums[:-1]))
