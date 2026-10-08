class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for j in range(N):
                matrix[r][j] = 0

        for c in cols:
            for i in range(M):
                matrix[i][c] = 0
