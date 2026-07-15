class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            v = target - nums[i]
            if v in seen:
                return [seen[v],i]
            seen[nums[i]] = i
        return [-1,-1]
