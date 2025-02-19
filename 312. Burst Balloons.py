# 312. Burst Balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]
        dp = {}
            
        def dfs(l, r):
            if r < l:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            res = 0
            for i in range(l, r + 1):
                coin = nums[l - 1] * nums[i] * nums[r + 1]
                coin += dfs(l, i - 1) + dfs(i + 1, r)
                res = max(res, coin)

            dp[(l, r)] = res 
            return res
        
        return dfs(1, len(nums) - 2)