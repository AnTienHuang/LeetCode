# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        insert_index = len(intervals)
        updates = []
        res = intervals.copy()
        ns, ne = newInterval
        if not intervals:
            return [newInterval]
        if ne < intervals[0][0]:
            return [newInterval] + intervals
        for i in range(len(intervals)):
            s, e = intervals[i]
            if (ns <= s and s <= ne) or (ns <= e and e <= ne):
                insert_index = min(insert_index, i)
                updates.append([s, e])
                res.remove([s, e])
            elif s < ns and ne < e:
                return intervals
            elif i < len(intervals) - 1 and e < ns and ne < intervals[i + 1][0]:
                intervals.insert(i + 1, newInterval)
                return intervals

        while updates:
            us, ue = updates.pop()
            ns = min(ns, us)
            ne = max(ne, ue)
        
        res.insert(insert_index, [ns, ne])
        return res
