class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse = True)
        prev = (target - pairs[0][0])/pairs[0][1]
        fleet = 1
        for p,s in pairs[1:]:
            cur = (target - p)/s
            if cur > prev:
                fleet += 1
                prev = cur
        return fleet