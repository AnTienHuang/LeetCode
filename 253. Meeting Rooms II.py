# 253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        heap = [intervals[0][1]]
        for i in intervals[1:]:
            start, end = i
            q = []
            while heap:
                min_end = heapq.heappop(heap)
                if start < min_end:
                    q.append(min_end)
                else:
                    break
            heapq.heappush(heap, end)
            while q:
                n = q.pop()
                heapq.heappush(heap, n)
        return len(heap)
