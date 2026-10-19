class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        k = n // 3
        ans = set()
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
            if count[i] > k:
                ans.add(i)
        return list(ans)