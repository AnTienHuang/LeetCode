# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set() 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        r, c = 0, 0
        turn = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        while len(res) < ROWS * COLS:
            res.append(matrix[r][c])
            visited.add((r, c))
            nr, nc = r + turn[i % 4][0], c + turn[i % 4][1]
            if ((nr, nc) in visited or 
                nr < 0 or nr == ROWS or
                nc < 0 or nc == COLS
            ):
                i += 1
                r, c = r + turn[i % 4][0], c + turn[i % 4][1]
            else:
                r = nr
                c = nc
        
        return res
