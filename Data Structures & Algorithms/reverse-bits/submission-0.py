class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            r = (n >> i) & 1
            ans += (r << (31-i))
        return ans