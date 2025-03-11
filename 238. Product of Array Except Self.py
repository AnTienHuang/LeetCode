# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = forward
            forward *= nums[i]
        backward = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= backward
            backward *= nums[i]
        
        return res
        