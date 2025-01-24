import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        ans = r
        while r >= l:
            k = (l + r) // 2
            if k == 0:
                break
            time = 0

            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
        
        return ans
            