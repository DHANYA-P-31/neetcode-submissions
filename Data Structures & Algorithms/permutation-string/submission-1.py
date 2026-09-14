class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d ={}
        if len(s1) > len(s2):
            return False
        for i in s1:
            d[i] = d.get(i,0) + 1
        l = 0
        r = len(s1)
        t = {}
        for i in s2[l:r-1]:
            t[i] = t.get(i,0)+1
        for i in s2[r-1:]:
            t[i] = t.get(i,0)+1
            print(d,t)
            if t == d:
                return True
            t[s2[l]] -= 1
            if t[s2[l]]==0:
                del t[s2[l]]
            l+=1
        return False
            