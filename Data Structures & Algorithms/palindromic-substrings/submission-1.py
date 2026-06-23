class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [0]
        def expand(l,r): 
            while l >= 0 and r<len(s) and s[l] == s[r]:
                res[0] += 1
                l-=1
                r+=1
            return s[l+1:r]
        n = len(s)
        for i in range(n):
            p1 = expand(i,i+1)
            p2 = expand(i,i)
        return res[0]