class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        pos = 1
        i = 0
        n = len(nums)
        while i < n and nums[i] <=0:
            i+=1
        while i < n:
            if nums[i] != pos:
                return pos
            while i<n-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
            pos += 1
        return pos