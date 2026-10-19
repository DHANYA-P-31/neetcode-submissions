class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        presum = 0
        d = {0:1}

        for num in nums:
            presum += num
            dif = presum - k
            res += d.get(dif,0)
            d[presum] = d.get(presum,0) + 1
        return res