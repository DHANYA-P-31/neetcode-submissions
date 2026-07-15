class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                d[i]+=1
        heap  =  []
        for n in d:
            heapq.heappush(heap,(d[n],n))
            if len(heap) > k:
                heapq.heappop(heap)
        v = []
        for h in heap:
            v.append(h[1])
        return v