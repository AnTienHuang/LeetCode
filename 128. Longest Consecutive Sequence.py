# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n - 1 not in nums:
                l = 1
                while n + l in nums:
                    l += 1
                res = max(l, res) 

        return res
        