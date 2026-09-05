class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        ans  = 0
        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]]+1,l)
            d[s[r]] = r
            ans = max(ans,r - l + 1)
        return ans