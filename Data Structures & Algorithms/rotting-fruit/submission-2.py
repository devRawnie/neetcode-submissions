class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        R = len(grid)
        C = len(grid[0])
        ones = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        ans = 0
        directions = [
            (1,0),
            (-1,0),
            (0, 1),
            (0, -1)
        ]
        while q:
            r, c, t = q.popleft()
            if grid[r][c] == -2 or grid[r][c] == 0:
                continue

            ans = max(ans, t)
            grid[r][c] = -2
            for dx, dy in directions:
                nx = r + dx
                ny = c + dy
                if nx < 0 or nx >= R:
                    continue

                if ny < 0 or ny >= C:
                    continue
                
                q.append((nx, ny, t+1))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return ans
                