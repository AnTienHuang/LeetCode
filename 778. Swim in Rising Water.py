# 778. Swim in Rising Water
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return 0
            
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        heap = [(grid[0][0], 0, 0)] # (value, r, c)

        heapq.heapify(heap)
        min_t = 0

        while heap:
            v, r, c = heapq.heappop(heap)
            min_t = max(min_t, v)

            if (r == ROWS - 1 and c == COLS - 2 or
                r == ROWS - 2 and c == COLS - 1): # we are reaching the bottom left
                min_t = max(min_t, grid[-1][-1])
                return min_t
            
            visited.add((r, c))

            if (r + 1, c) not in visited and r + 1 < ROWS:
                heapq.heappush(heap, (grid[r + 1][c], r + 1, c))
            if (r - 1, c) not in visited and r - 1 >= 0:
                heapq.heappush(heap, (grid[r - 1][c], r - 1, c))
            if (r, c + 1) not in visited and c + 1 < COLS:
                heapq.heappush(heap, (grid[r][c + 1], r, c + 1))
            if (r, c - 1) not in visited and c - 1 >= 0:
                heapq.heappush(heap, (grid[r][c - 1], r, c - 1))
                
