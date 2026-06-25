class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        result = []

        def safe(r, c):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row = r-1
            col = c-1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row = r-1
            col = c+1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True


        def dfs(i):
            if i == n:
                b = ["".join(br) for br in board]
                result.append(b)
                return

            for j in range(n):
                if safe(i, j):
                    board[i][j] = "Q"
                    dfs(i+1)
                    board[i][j] = "."

        dfs(0)
        return result

