# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if matrix[i][0] <= target <= matrix[i][-1]:
                break
            i += 1
        if i == len(matrix):
            return False
        # return target in matrix[i] 

        nums = matrix[i]
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (r + l) // 2
            if m == l or m == r:
                return target == nums[r] or target == nums[l]
            elif nums[m] > target:
                r = m - 1
            else:
                l = m
