class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        if len(height) < 3:
            return res
        l = 0
        r = len(height) - 1
        l_max = height[0] 
        r_max = height[-1]

        while (l < r): 
            if l_max > r_max:
                r -= 1
                res += max(r_max - height[r], 0)
                r_max = max(r_max, height[r])
            else:
                l += 1
                res += max(l_max - height[l], 0)
                l_max = max(l_max, height[l])

        return res


