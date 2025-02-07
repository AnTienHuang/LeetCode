# 416. Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        T = sum(nums)
        if T % 2 != 0:
            return False
        T = T / 2

        sums = {0} # tracking all possible sums for a partition
        for n in nums:
            sums_copy = sums.copy()
            for s in sums: 
                if s + n == T:
                    return True
                sums_copy.add(s + n)
            sums = sums_copy
        
        return False