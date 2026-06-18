class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        ans = 0
        most_frequent = 0
        l = 0
        n = len(s)
        for r in range(n):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            most_frequent = max(freq[s[r]],most_frequent)
            while (r - l + 1) > (most_frequent+k):
                freq[s[l]] -= 1
                l += 1
            ans = max(ans,r - l + 1)
        return ans