class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(l,r,target):
            while l <= r:
                mid = l +(r-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid +1
                else:
                    r = mid-1
            return -1
        n = len(nums)
        l,r = 0,n-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        if target <= nums[n-1]:
            return bin_search(r,n-1,target)
        else:
            return bin_search(0,r,target)
