class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        i = -3
        while -i < len(cost) + 1:
            cost[i] += min(cost[i+1], cost[i+2])
            i -= 1
        return min(cost[0], cost[1])