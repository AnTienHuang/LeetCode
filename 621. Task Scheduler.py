class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-v for v in counter.values()]
        q = deque()
        time = 0
        heapq.heapify(heap)
        while heap or q:
            if heap:
                i = heapq.heappop(heap)
                i += 1
                if i < 0:
                    q.append([i, time + n])
            
            if q:
                if q[0][1] == time:
                    i, cd = q.popleft()
                    heapq.heappush(heap, i)

            time += 1
        return time
