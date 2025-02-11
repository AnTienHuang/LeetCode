# 518. Coin Change II

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp0 = [0 for _ in range(amount + 1)]
        dp1 = dp0.copy()
        dp0[-1] = 1
        for c in coins:
            for a in range(1, amount + 1):
                i = -(a + 1)
                if a - c >= 0:
                    dp0[i] += dp0[-(a - c + 1)]
                dp0[i] += dp1[i]
            dp1 = dp0.copy()
            dp0 = [0 for _ in range(amount + 1)]
            dp0[-1] = 1
        
        return dp1[0]
