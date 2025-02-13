# 97. Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i == len(s1) and j == len(s2) and (i + j) == len(s3):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False

            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)
            
            if j < len(s2) and s2[j] == s3[i + j]:
                res = res or dfs(i, j + 1)
            
            dp[(i, j)] = res

            return res

        return dfs(0, 0)