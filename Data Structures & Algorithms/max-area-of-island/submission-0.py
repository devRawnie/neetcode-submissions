class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[0]):
                return 0

            if not grid[i][j]:
                return 0

            # print('dfs', i,j)
            grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    # print('going in for', i, j)
                    total_area = dfs(i, j)
                    # print(total_area)
                    max_area = max(max_area, total_area)

        return max_area