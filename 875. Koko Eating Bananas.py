# 875. Koko Eating Bananas
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 2nd attempt
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (r + l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            if time > h:
                l = m + 1
            else:
                r = m - 1
                ans = min(ans, m)
        
        return ans

        # 1st attempt
        # l, r = 0, max(piles)
        # ans = r
        # while r >= l:
        #     k = (l + r) // 2
        #     if k == 0:
        #         break
        #     time = 0

        #     for p in piles:
        #         time += math.ceil(p / k)
        #     if time <= h:
        #         ans = min(ans, k)
        #         r = k - 1
        #     else:
        #         l = k + 1
        
        # return ans
            