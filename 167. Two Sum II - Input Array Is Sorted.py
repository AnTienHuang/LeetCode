# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            if target - numbers[i] in numbers[i + 1:]:
                return [i + 1, i + numbers[i + 1:].index(target - numbers[i]) + 2]
            else:
                while numbers[i + 1] == numbers[i]:
                    i += 1
            i += 1
