class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        maxFreq = 0
        d = {}
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0) + 1
            maxFreq = max(maxFreq,d[s[r]])
            while (r-l+1) > maxFreq+k:
                d[s[l]] -= 1
                l+=1
            ans = max(ans,r-l+1)
        return ans