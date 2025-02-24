# 252. Meeting Rooms
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        min_r = intervals[0][1]
        for i in intervals[1:]:
            l, r = i
            if l >= min_r:
                min_r = r
            else:
                return False
        return True