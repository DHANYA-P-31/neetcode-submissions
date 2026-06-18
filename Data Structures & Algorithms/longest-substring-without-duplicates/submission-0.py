class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        if s == "":
            return 0
        ans = 1
        n = len(s)
        d = {}
        for i in range(n):
            v = s[i]
            if v in d and d[v] >= r:
                ans = max(ans,i-r)
                r = d[v]+1
            d[v] = i
        ans = max(ans,n-r)
        return ans

            