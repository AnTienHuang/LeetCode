# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        min_end = intervals[0][1]

        for i in intervals[1:]:
            if i[0] < min_end:
                res += 1
                min_end = min(min_end, i[1])
            else:
                min_end = i[1]
        
        return res
        