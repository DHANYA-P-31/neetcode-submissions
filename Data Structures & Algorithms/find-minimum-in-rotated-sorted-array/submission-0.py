class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid 
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            else:
                return min(nums[l],nums[r])
        return nums[r]
