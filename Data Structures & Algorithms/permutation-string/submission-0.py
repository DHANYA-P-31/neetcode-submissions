class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        for i in s1:
            freq1[i] = 1+freq1.get(i,0)
        i = 0
        while i < n1:
            freq2[s2[i]] = 1+freq2.get(s2[i],0)
            i += 1
        while i < n2:
            if freq1 == freq2:
                return True
            freq2[s2[i-n1]] -= 1
            if freq2[s2[i-n1]] == 0:
                del freq2[s2[i-n1]]
            freq2[s2[i]] = 1 + freq2.get(s2[i],0)
            i += 1
        return freq1 == freq2
