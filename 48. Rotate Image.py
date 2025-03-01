# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # tracking indexes
        top = 0
        left = 0
        right = n - 1
        bot = n - 1

        for i in range(n - 1): # there will be at most n - 1 series of rotation
            if left < right:
                for k in range(right - left): # each serie have n - 1 rotation
                    tmp = matrix[top][left + k]
                    matrix[top][left + k] = matrix[bot - k][left]
                    matrix[bot - k][left] = matrix[bot][right - k]
                    matrix[bot][right - k] = matrix[top + k][right]
                    matrix[top + k][right] = tmp
                left += 1
                right -= 1
                bot -= 1
                top += 1
        