class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(x, y, pos):
            if pos == len(word):
                return True

            if x < 0 or x >= R:
                return False
            if y < 0 or y >= C:
                return False
            
            if board[x][y] == '#':
                return False
            
            if board[x][y] != word[pos]:
                return False

            curr = board[x][y]
            print('curr', curr)
            board[x][y] = "#"
            if dfs(x+1, y, pos+1):
                return True

            if dfs(x-1, y, pos+1):
                return True

            if dfs(x, y+1, pos+1):
                return True

            if dfs(x, y-1, pos+1):
                return True

            board[x][y] = curr

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False
