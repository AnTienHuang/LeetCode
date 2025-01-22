class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = [float("inf")] * n
        visited = set()
        minH = [(0, k)]
        while minH:
            w, i = heapq.heappop(minH) 
            if i in visited:
                continue
            dist[i-1] = w
            visited.add(i)
            for i2, w2 in adj[i]:
                if i2 not in visited:
                    heapq.heappush(minH, (w + w2, i2))
            
        return max(dist) if len(visited) == n else -1
