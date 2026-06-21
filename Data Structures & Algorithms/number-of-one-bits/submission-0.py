class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ""
        weight = 0
        while n!=0:
            r = n%2
            if r == 1:
                weight+=1
            n= n//2
        return weight