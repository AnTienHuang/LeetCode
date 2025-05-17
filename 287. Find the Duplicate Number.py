# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  
        # 2nd attempt
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2


        # 1st attempt
        # count = {}
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     if count[n] == 2:
        #         return n