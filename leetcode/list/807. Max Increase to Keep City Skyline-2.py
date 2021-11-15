# zip 을 이용

# 미리 만들어 놓고 시작해서 리소스, 시간 절약

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowsMax = [max(row) for row in grid]
        columnsMax = [max(col) for col in zip(*grid)]

        increased = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                increased += min(rowsMax[i], columnsMax[j]) - grid[i][j]
        return increased
