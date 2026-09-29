class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(i+1, C):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(R):
            for j in range(C//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][C-j-1]
                matrix[i][C-j-1] = temp
