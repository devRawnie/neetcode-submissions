class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n - 1
        while l < r:
            mid = l + (r-l)//2
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            if target == val:
                return True
            
            if target < val:
                r = mid - 1
            else:
                l = mid + 1

        row = l // n
        col = l % n
        if matrix[row][col] == target:
            return True

        row = r // n
        col = r % n
        if matrix[row][col] == target:
            return True

        return False