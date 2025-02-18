# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            max_r = 0
            for i in range(l, r + 1):
                max_r = max(max_r, nums[i] + i)
            l = r + 1
            r = max_r
            res += 1
        
        return res
