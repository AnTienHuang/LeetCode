# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int: 
    # 2nd attempt
        res = 0

        l = 0
        r = len(height) - 1

        while r > l:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

    # 1st attempt
        # if len(height) < 2:
        #     return 0
        # res = 0
        # l, r = 0, len(height) - 1
        # while r > l:
        #     res = max(res, min(height[l], height[r]) * (r - l))
        #     if height[r] > height[l]:
        #         l += 1
        #     else:
        #         r -= 1
        
        # return res
