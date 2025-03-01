# 1851. Minimum Interval to Include Each Query
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {} # hash map for query: length
        i = 0 # tracking index of intervals
        heap = [] # (size of interval, right end of the interval)
        intervals.sort()

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q: # add interval to heap if the min value of interval <= q
                heapq.heappush(heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1
            while heap and heap[0][1] < q: # remove invalid values from the heap
                heapq.heappop(heap)
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1
        
        return [res[q] for q in queries]