class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        while n > 1 and i <996:
            temp = n
            n = 0
            while temp > 0:
                k = temp % 10
                n += k*k
                temp = temp // 10
            i += 1
        return True if n == 1 else False