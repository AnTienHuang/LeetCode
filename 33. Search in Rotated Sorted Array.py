# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: #nums[m] < nums[l]
                if target < nums[m] or target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1