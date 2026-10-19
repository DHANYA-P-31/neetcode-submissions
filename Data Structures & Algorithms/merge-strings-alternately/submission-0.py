class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i,j = 0,0
        s = ""
        while i < n and j < m:
            s+=word1[i]+word2[j]
            i+=1
            j+=1
        if i < n:
            s += word1[i:]
        if j < m:
            s+= word2[j:]
        return s