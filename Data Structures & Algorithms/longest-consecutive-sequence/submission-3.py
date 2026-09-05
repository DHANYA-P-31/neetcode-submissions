class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        n = len(nums)
        i = 0
        if n == 0:
            return 0
        while i+1 < n:
            cur_max = 1
            while i+1 < n and nums[i+1] - nums[i] <= 1:
                if nums[i+1] - nums[i] == 1:
                    cur_max += 1
                i += 1
            i += 1
            ans = max(ans,cur_max)
        return ans
            
        