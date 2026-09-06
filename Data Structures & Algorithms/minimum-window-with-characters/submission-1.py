class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = {}
        for i in t:
            dt[i] = dt.get(i,0) + 1
        l = 0
        min_len = float('inf')
        best_l,best_r = 0,0
        n = len(s)
        d = {}
        required = len(dt)
        formed = 0
        for r in range(n):
            i = s[r]
            if i in dt:
                d[i] = d.get(i,0)+1
                if d[i] == dt[i]:
                    formed+=1
                while formed == required:
                    if min_len > (r-l+1):
                        min_len = r - l +1
                        best_l = l
                        best_r = r
                    ch = s[l]
                    if ch in dt:
                        if d[ch] == dt[ch]:
                            formed -=1
                        d[ch] -= 1
                    l += 1
        if min_len == float('inf'):
            return ""

        return s[best_l:best_r+1]
                