class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])

        t = 0
        r = N-1
        l = 0
        b = M-1
        print(t, l, b, r)
        result = []
        while len(result) < M*N:
            # Top row
            # print('1', t, l, b, r, result)
            for i in range(l, r+1):
                result.append(matrix[t][i])
            t += 1

            print('1', t, l, b, r, result)
            # Right column
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1

            if l > r or t > b:
                break
            print('2', t, l, b, r, result)
            # Bottom Row
            for i in range(r, l-1, -1):
                result.append(matrix[b][i])
            b -= 1

            print('3', t, l, b, r, result)
            # Left Column
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l += 1
            print('4', t, l, b, r, result)

        return result
