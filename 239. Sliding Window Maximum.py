# 239. Sliding Window Maximum
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = {}
        max_value = nums[0]
        for i in range(k):
            if nums[i] > max_value:
                max_value = nums[i]
            window[nums[i]] = 1 + window.get(nums[i], 0)
        res = [max_value]

        l = 0
        for r in range(k, len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                window.pop(nums[l])
                if nums[l] == max_value:
                    max_value = max(window.keys())
            l += 1
            max_value = max(nums[r], max_value)
            res.append(max_value)

        return res
                