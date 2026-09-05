class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in d:
                return [d[v],i]
            d[nums[i]] = i
        return [-1,-1]
        