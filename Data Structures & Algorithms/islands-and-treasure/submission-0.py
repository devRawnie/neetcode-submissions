class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r,c))

        def addCell(i,j):
            if i < 0 or i >= R:
                return
            if j < 0 or j >= C:
                return
            if (i,j) in visited:
                return
            if grid[i][j] == -1:
                return

            q.append((i,j))
            visited.add((i,j))

        d = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = d

                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            d += 1

