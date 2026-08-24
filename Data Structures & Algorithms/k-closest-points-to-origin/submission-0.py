class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i,j in points:
            val = -(i**2+j**2)
            heapq.heappush(minHeap,[val,i,j])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        ans = [x[1:] for x in minHeap]
        return ans
