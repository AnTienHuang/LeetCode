# 763. Partition Labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        sum_res = 0
        boundary = {}
        for i, n in enumerate(s):
            boundary[n] = i
        b = boundary[s[0]]

        for i, n in enumerate(s):
            if boundary[n] > b:
                b = boundary[n]
                continue
            if i == b:
                res.append(i + 1 - sum_res)
                sum_res = i + 1
                b = boundary[s[i + 1]] if i < len(s) - 1 else 0

        return res
