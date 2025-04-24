# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
    # 2nd attempt
        if len(prices) < 2: return 0
        res = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res

    # 1st attempt
    #     l, r = 0, 1
    #     res = 0
    #     while r < len(prices):
    #         if prices[r] < prices[l]:
    #             l = r
    #             r = l + 1
    #         else:
    #             res = max(res, prices[r] - prices[l])
    #             r += 1

    #     return res
