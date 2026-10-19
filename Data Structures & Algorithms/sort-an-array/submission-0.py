class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,l,m,r):
            left,right = nums[l:m+1],nums[m+1:r+1]
            i,j,k = 0,0,l
            while i< len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                nums[k] = left[i]
                k+=1
                i+=1
            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1
        def mergeSort(nums,l,r):
            if l >= r:
                return
            mid = l + (r-l)//2
            mergeSort(nums,l,mid)
            mergeSort(nums,mid+1,r)
            merge(nums,l,mid,r)
        mergeSort(nums,0,len(nums)-1)
        return nums
        