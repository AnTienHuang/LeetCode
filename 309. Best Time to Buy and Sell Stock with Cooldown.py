# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        hold, sell, rest = -float('inf'), 0, 0
        
        for price in prices:
            prev_sell = sell  # Store previous sell state before updating
            sell = hold + price  # If we sell today, we must have held stock before
            hold = max(hold, rest - price)  # Either keep holding or buy today
            rest = max(rest, prev_sell)  # Cooldown from previous sell or stay in rest

        return max(sell, rest)  # Max profit is in sell or rest, never in hold
