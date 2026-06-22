class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        i = 0
        count = 0
        dp =  [[0]*(l2+1) for _ in range(l1+1)]
        while i<l1:
            j = 0
            while j<l2:
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
                j += 1
            i += 1
        return dp[l1][l2]


