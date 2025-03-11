# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        # check row
        for r in board:
            for s in r:
                if s == ".":
                    continue
                if s in visited:
                    return False
                visited.add(s)
            visited = set()
        
        # check col
        for c in range(9):
            for r in range(9):
                s = board[r][c]
                if s == ".":
                    continue
                if s in visited:
                    return False
                visited.add(s)
            visited = set()
        
        # check 3x3 grid
        centers = ((1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (1, 7), (4, 7), (7, 7))
        dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for r, c in centers:
            if board[r][c] != ".":
                visited.add(board[r][c])
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if board[nr][nc] == ".":
                    continue
                if board[nr][nc] in visited:
                    return False
                visited.add(board[nr][nc])
            visited = set()

        return True
