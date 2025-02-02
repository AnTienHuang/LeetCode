class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        dp = { c: 1 for c in coins } 
        dp[0] = 0
        coins.sort()
        def dfs(i):
            if i in dp:
                return dp[i]
            if i < coins[0]:
                dp[i] = -1
                return dp[i]
            nums = [dfs(i - c) for c in coins]
            if any(x > -1 for x in nums):
                dp[i] = 1 + min(x for x in nums if x > -1)
            else:
                dp[i] = -1
            return dp[i]
        dfs(amount)
        return dp[amount]