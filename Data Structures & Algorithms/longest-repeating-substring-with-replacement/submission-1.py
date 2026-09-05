class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        most_frequent = 0
        l = 0
        n = len(s)

        for r in range(n):
            d[s[r]] = d.get(s[r],0) + 1
            most_frequent = max(most_frequent,d[s[r]])
            while (r-l+1) > most_frequent+k:
                d[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
        return ans