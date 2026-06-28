class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in nums:
            heapq.heappush(q,i)
            if len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q)
