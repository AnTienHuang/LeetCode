# 15. 3Sum
class Solution:
    def threeSum(self, numbers: list[int]) -> list[int]:
        res = []
        numbers.sort()

        for i, n in enumerate(numbers):
            if i > 0 and n == numbers[i - 1]:
                continue
            
            l = i + 1
            r = len(numbers) - 1

            while r > l:
                k = n + numbers[r] + numbers[l]
                if k > 0:
                    r -= 1
                elif k < 0:
                    l += 1
                else:
                    res.append([n, numbers[l], numbers[r]])
                    l += 1
                    while numbers[l] == numbers[l - 1] and l < r:
                        l += 1
        
        return res
