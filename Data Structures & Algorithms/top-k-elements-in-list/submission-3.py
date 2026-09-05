class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)

        h = []
        for n in count.keys():
            heapq.heappush(h,(count[n],n))
            if len(h) > k:
                heapq.heappop(h)
        
        return list(i[1] for i in h)