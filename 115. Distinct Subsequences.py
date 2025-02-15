# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, k):
            if k == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, k) in dp:
                return dp[(i, k)]
            
            res = dfs(i + 1, k)
            if s[i] == t[k]:
                res += dfs(i + 1, k + 1)
            dp[(i, k)] = res
            return res
        
        return dfs(0, 0)
