# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            if 0 in matrix[r]:
                matrix[r] = [0 if n == 0 else float("inf") for n in matrix[r]]
        
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for i in range(ROWS):
                        matrix[i][c] = float("inf") if matrix[i][c] != 0 else 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float("inf"):
                    matrix[r][c] = 0
            