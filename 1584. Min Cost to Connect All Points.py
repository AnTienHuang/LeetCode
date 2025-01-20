class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        n = len(points)
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, w))
                adj[j].append((i, w))
        # print(adj)
        minH = [(0, 0)] # min heap for (distance, point_index)
        visited = set()
        res = 0
        while minH:
            w, p = heapq.heappop(minH)
            if p in visited:
                continue
            visited.add(p)
            res += w
            for point, weight in adj[p]:
                if point not in visited:
                    heapq.heappush(minH, (weight, point))
        return res
