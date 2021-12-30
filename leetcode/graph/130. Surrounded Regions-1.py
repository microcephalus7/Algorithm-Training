# 그래프에서 둘러싸인 요소 바꾸기
# DFS
# 실패
# 보충 필요

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if board[i][j] == 'O' and i > 0 and i < len(board) - 1 and j > 0 and j < len(board[0]) - 1:
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

                board[i][j] = "X"

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O':
                    dfs(i, j)
