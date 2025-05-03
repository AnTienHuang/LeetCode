# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        cur = [heights[0], 1]
        res = 0
        for i, h in enumerate(heights[1:], start=1):
            height, length = cur
            if h > (height * (length + 1)):
                cur = [h, 1]
            elif min(height, h) * (length + 1) > height * length:
                cur = [min(height, h), length + 1]
            res = max(res, cur[0] * cur[1])
            # print(cur)
        
        return res
