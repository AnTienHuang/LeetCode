# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n ==1:
            return 1

        dp = [[-1] * n] * m 
        for i in range(n):
            dp[-1][i] = 1
        for i in range(m):
            dp[i][-1] = 1

        for i in range(m - 2, -1, -1):
            for k in range(n - 2, -1, -1):
                dp[i][k] = dp[i - 1][k] + dp[i][k + 1]
        
        return dp[0][0]