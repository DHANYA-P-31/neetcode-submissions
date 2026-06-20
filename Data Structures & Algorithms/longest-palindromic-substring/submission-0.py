class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def expand(l,r): 
            while l >= 0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        n = len(s)
        for i in range(n):
            p1 = expand(i,i+1)
            p2 = expand(i,i)
            ans = max(ans,p1,p2,key = len)
        return ans