class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e+="$"+str(len(s))+"#"+s
        return e

    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        if len(s) == 0:
            return []
        while i < len(s):
            if s[i] == "$":
                i += 1
                n = ""
                while s[i] != "#":
                    n+=s[i]
                    i+=1
                i += 1
                num = int(n)
                l.append(s[i:i+num])
                i += num
        return l