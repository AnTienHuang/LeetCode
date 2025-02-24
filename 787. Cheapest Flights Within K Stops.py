# 787. Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list) # src: [(dst, cost)]
        for f in flights:
            adj[f[0]].append((f[1], f[2]))

        dp = {}
        heap = [(0, src, k + 1)]
        while heap:
            cost, ori, stops = heappop(heap)
            if ori == dst:
                return cost
            if stops > 0:
                for neighbor, price in adj[ori]:
                    new_cost = price + cost
                    if (neighbor, stops - 1) not in dp or new_cost < dp[(neighbor, stops -1)]:
                        dp[(neighbor, stops - 1)] = new_cost
                        heappush(heap, (new_cost, neighbor, stops - 1))
        
        return -1
