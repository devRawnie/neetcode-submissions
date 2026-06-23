class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            seen.clear()
            for j in range(9):
                val = board[i][j]
                if val != "." and val in seen:
                    return False
                seen.add(val)

        for i in range(9):
            seen.clear()
            for j in range(9):
                val = board[j][i]
                if val != "." and val in seen:
                    return False
                seen.add(val)

        for sq in range(9):
            seen.clear()
            for i in range(3):
                for j in range(3):
                    r = (sq//3) * 3 + i
                    c = (sq%3) * 3 + j
                    val = board[r][c]
                    if val != "." and val in seen:
                        return False
                    seen.add(val)

        return True

