class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0

        for row_index in range(len(grid)):
            for column_index in range(len(grid[0])):
                max_row = max(grid[row_index])
                max_column = max([row[column_index] for row in grid])

                result += min(max_row, max_column) - \
                    grid[row_index][column_index]

        return result
