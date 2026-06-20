class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        f1,f2 = 1,2
        cur = 0
        for _ in range(3,n+1):
            cur = f1 + f2
            f1 = f2
            f2 = cur
        return cur