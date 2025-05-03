# 704. Binary Search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i = 0
        while l <= r and i < len(nums):
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target == nums[r]:
                return r
            if target == nums[l]:
                return l
            if target > nums[mid]:
                l = mid
            else:
                r = mid
            i += 1
        return -1
    