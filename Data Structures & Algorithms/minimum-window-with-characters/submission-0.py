class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        best_len = float('inf')
        best_r = 0
        best_l = 0
        if n<m or n==0:
            return ""
        d = {}
        l = 0
        need = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        required = len(need)
        formed = 0
        for r in range(n):
            i = s[r]
            if i in need:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                if d[i] == need[i]:
                    formed += 1
                while formed == required:
                    if best_len > (r-l+1):
                        best_len = r-l+1
                        best_l = l
                        best_r = r
                    ch = s[l]
                    if ch in need:
                        if d[ch] == need[ch]:
                            formed -= 1
                        d[ch] -= 1
                    l+=1
        if best_len == float('inf'):
            return ""
        return s[best_l:best_r+1]
            