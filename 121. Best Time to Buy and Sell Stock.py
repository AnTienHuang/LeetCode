# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1

        return res
