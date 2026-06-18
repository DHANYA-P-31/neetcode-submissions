class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1
        n = len(nums)
        curr = 1
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(longest,curr)
                curr = 1
        longest = max(longest,curr)
        return 0 if n == 0 else longest
