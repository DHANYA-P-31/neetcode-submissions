class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                d.remove(i)
        return d.pop()