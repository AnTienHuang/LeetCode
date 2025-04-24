# 42. Trapping Rain Water
class Solution:
    def trap(self, height: list[int]) -> int: 
    # 2nd attempt
        if len(height) < 3:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while r > l:
            if height[r] < height[l]:
                r -= 1
                res += max(0, min(max_l, max_r) - height[r])
                max_r = max(height[r], max_r)
            else:
                l += 1
                res += max(0, min(max_l, max_r) - height[l])
                max_l = max(height[l], max_l)
        
        return res

    # 1st attempt
        # res = 0
        # if len(height) < 3:
        #     return res
        # l = 0
        # r = len(height) - 1
        # l_max = height[0] 
        # r_max = height[-1]

        # while (l < r): 
        #     if l_max > r_max:
        #         r -= 1
        #         res += max(r_max - height[r], 0)
        #         r_max = max(r_max, height[r])
        #     else:
        #         l += 1
        #         res += max(l_max - height[l], 0)
        #         l_max = max(l_max, height[l])

        # return res


