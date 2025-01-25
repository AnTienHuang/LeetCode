class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.max_rob(nums[1:]), self.max_rob(nums[:-1])) # have to add nums[0] to handle edge case where len(nums) == 1
        
    def max_rob(self, nums: List[int]) -> int:
        tmp1, tmp2 = 0, 0
        for n in nums:
            max_val = max(tmp1 + n, tmp2) 
            tmp1 = tmp2
            tmp2 = max_val
        return tmp2