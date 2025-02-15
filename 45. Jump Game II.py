# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        goal = len(nums) - 1
        dp = {} # index: min jumps to goal

        for i in range(goal - 1, -1, -1):
            if nums[i] + i >= goal:
                dp[i] = 1
                continue
            j = float("inf")
            for k in range(1, nums[i] + 1):
                j = min(j, 1 + dp[k + i])
            dp[i] = j
        
        return dp[0]