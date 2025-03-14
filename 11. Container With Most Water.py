# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int: 
        if len(height) < 2:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        while r > l:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return res
