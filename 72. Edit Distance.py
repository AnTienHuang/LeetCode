# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [i for i in range(len(word1), -1, -1)]
        k = 1
        for i in range(len(word2) - 1, -1, -1):
            next_dp = [k] * (len(word1) + 1)
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = 1 + min(next_dp[j + 1], dp[j], dp[j + 1])
            dp = next_dp
            k += 1

        return dp[0]