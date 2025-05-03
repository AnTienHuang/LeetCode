# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while r >= l:
            m = (l + r) // 2
            if m == r or m == l:
                return min(nums[r], nums[l])
            if nums[r] > nums[m]:
                r = m
            else:
                l = m
                