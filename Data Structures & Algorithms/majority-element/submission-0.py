class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums) // 2 + 1
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
            if count[n] == m:
                return n