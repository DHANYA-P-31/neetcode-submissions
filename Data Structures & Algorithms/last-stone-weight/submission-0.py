class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x =-(heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            print(x,y)
            if x != y:
                heapq.heappush(stones,y - x)
        return 0 if len(stones) == 0 else -stones[0]
        