# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # value: index
        for i, n in enumerate(nums):
            if (target - n) in visited:
                return [i, visited[target - n]]
            else:
                visited[n] = i
            