class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        y = abs(x)
        while y>0 :
            rem = y % 10                
            ans = ans*10 + rem
            y//=10
        if x<0:
            ans = -ans
        if ans>(2**31-1) or ans<-(2**31):
            return 0
        return ans