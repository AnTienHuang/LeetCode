# 494. Target Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        if target > sum(nums) or target < -sum(nums):
            return 0

        for n in nums:
            next_dp = defaultdict(int)
            for k in dp:
                next_dp[k + n] += dp[k]
                next_dp[k - n] += dp[k]
            dp = next_dp

        return dp[target]
