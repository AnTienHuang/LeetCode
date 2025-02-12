# 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1) + 1)
        for i in range(len(text2) - 1, -1, -1):
            next_dp = [0] * (len(text1) + 1)
            for k in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[k]:
                    next_dp[k] = dp[k + 1] + 1
                else:
                    next_dp[k] = max(dp[k], next_dp[k + 1])
            dp = next_dp

        return dp[0]