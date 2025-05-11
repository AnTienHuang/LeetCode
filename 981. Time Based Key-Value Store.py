# 981. Time Based Key-Value Store
class TimeMap:

    def __init__(self):
        self.store = {} # key : [[val1, timestamp1], [val2, timestamp2], ...]

    def set(self, key: str, val: str, timestamp: int):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([val, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        vals = self.store[key]
        l, r = 0, len(vals) - 1

        while r >= l:
            m = (r + l) // 2
            if vals[m][1] == timestamp:
                return vals[m][0]
            elif vals[m][1] > timestamp:
                r = m - 1
            else:
                res = vals[m][0]
                l = m + 1
        
        return res