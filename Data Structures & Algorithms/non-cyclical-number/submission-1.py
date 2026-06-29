class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1 and n not in seen:
            temp = n
            n = 0
            seen.add(temp)
            while temp > 0:
                k = temp % 10
                n += k*k
                temp = temp // 10
            
        return True if n == 1 else False