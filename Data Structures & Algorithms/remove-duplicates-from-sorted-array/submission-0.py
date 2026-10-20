class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,j = 0,1
        n = len(nums)
        while j < n:
            while j<n and nums[i] == nums[j]:
                j+=1
            if j==n:
                break
            i += 1
            nums[i] = nums[j]
            j += 1
        return i+1