class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n-1
        def binary_search(l,r,target):
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid-1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return mid
            return -1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        if target <= nums[n-1]:
            return binary_search(r,n-1,target)
        else:
            return binary_search(0,r-1,target)