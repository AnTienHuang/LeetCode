# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights): 
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                res = max(res, (i - index) * height)
            stack.append([start, h])
        
        while stack:
            index, height = stack.pop()
            res = max(res, (len(heights) - index) * height)

        return res
