class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = []

        def dfs(dst):
            if dst not in adj:
                res.append(dst)
                return
            while adj[dst]:
                nei = adj[dst].pop()
                dfs(nei)
            res.append(dst)
            return
        
        dfs("JFK")

        return res[::-1]