class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                d[i]+=1
        l = sorted(d,key = d.get,reverse = True)
        return l[:k]