# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ints = sorted(intervals, key=lambda x: x[0])
        res = [ints[0]]

        for i in range(1, len(ints)):
            s, e = res[-1]
            ns, ne = ints[i]
            if e < ns: # no overlap
                res.append(ints[i])
            elif s <= ns and ns <= e: # overlap
                res[-1][0] = min(s, ns)
                res[-1][1] = max(e, ne)
        
        return res
