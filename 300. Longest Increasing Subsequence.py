class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[] for _ in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            dp[i] = [nums[i]]
            for k in range(i):
                if nums[i] > dp[k][-1] and len(dp[k]) >= len(dp[i]):
                    dp[i] = dp[k] + [nums[i]]
                    res = max(res, len(dp[i]))
        
        return res
