# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(cur, open, close):
            if n == open == close:
                s = "".join(cur)
                res.append(s)
                return
            if open < n:
                cur.append("(")
                dfs(cur, open + 1, close)
                cur.pop()
            if close < open:
                cur.append(")")
                dfs(cur, open, close + 1)
                cur.pop()
            
        dfs([], 0, 0)
        return res
