class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs[0])
        i = 0
        flag = False
        while i < n:
            pre = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != pre:
                    flag = True
                    break
            if flag:
                break                
            ans += pre
            i += 1
        return ans