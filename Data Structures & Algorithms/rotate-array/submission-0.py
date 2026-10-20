class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k%n
        def rev(nums,l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l+= 1
                r -= 1
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n -1)