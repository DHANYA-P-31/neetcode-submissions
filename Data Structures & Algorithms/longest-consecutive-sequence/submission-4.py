class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        if n == 0:
            return 0

        ans = 1
        cur_max = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                cur_max += 1
            else:
                cur_max = 1

            ans = max(ans, cur_max)

        return ans